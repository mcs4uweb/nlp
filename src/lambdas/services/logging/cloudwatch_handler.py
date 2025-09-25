import boto3
import json
from botocore.exceptions import ClientError
from queue import Queue, Empty
from threading import Thread, Event
import logging
import atexit
import signal
import sys


class CloudWatchHandler(logging.Handler):
    """Custom logging handler that sends logs to CloudWatch asynchronously without batching"""
    
    STANDARD_LOG_ATTRIBUTES = {
        'asctime', 'created', 'exc_info', 'exc_text', 'filename',
        'funcName', 'levelname', 'levelno', 'lineno', 'message',
        'module', 'msecs', 'msg', 'name', 'pathname', 'process',
        'processName', 'threadName', 'thread', 'relativeCreated', 
        'args'
    }
    
    def __init__(
        self,
        log_group: str,
        log_stream: str,
        region_name: str,
        force_flush: bool = True
    ):
        """
        Initialize the CloudWatch handler.
        
        Args:
            log_group: CloudWatch log group name (must exist)
            log_stream: CloudWatch log stream name
            region_name: AWS region
            force_flush: Whether to force flush logs on shutdown
        """
        super().__init__()
        self.log_group = log_group
        self.log_stream = log_stream
        self.client = boto3.client('logs', region_name=region_name)
        self.sequence_token = None
        self.force_flush = force_flush
        
        self.log_queue = Queue()
        self.shutdown_event = Event()
        
        # Create new log stream
        self._create_log_stream()
        
        # Start background thread for log processing
        self.worker = Thread(target=self._log_sender, daemon=True)
        self.worker.start()

        # Register shutdown handlers
        if self.force_flush:
            atexit.register(self.flush_and_stop)
            # Handle Lambda container shutdown
            try:
                signal.signal(signal.SIGTERM, self._signal_handler)
            except ValueError:
                # Signal may not be available in all environments
                pass

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals by flushing logs without exiting the application."""
        self.flush_and_stop()
    
    def _create_log_stream(self) -> None:
        """Create log stream if it doesn't exist."""
        try:
            self.client.create_log_stream(
                logGroupName=self.log_group,
                logStreamName=self.log_stream
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise ValueError(f"Log group {self.log_group} does not exist. Please create it using infrastructure as code.")
            elif e.response['Error']['Code'] != 'ResourceAlreadyExistsException':
                raise
    
    def emit(self, record: logging.LogRecord) -> None:
        """Put log record into the queue for async processing."""
        try:
            log_entry = {
                'timestamp': int(record.created * 1000),
                'message': self.format(record),
                'extra': {
                    'level': record.levelname,
                    'caller': record.filename + ':' + record.funcName,
                    'event_type': record.event_type if hasattr(record, 'event_type') else None,
                    'recruit_process_id': record.recruit_process_id if hasattr(record, 'recruit_process_id') else None,
                    'dod_id': record.dod_id if hasattr(record, 'dod_id') else None,
                }
            }

            # Add any non-standard attributes to the extra dictionary
            for attr, value in record.__dict__.items():
                if attr not in self.STANDARD_LOG_ATTRIBUTES:
                    log_entry['extra'][attr] = value if hasattr(record, attr) else None
        
            self.log_queue.put(log_entry)
            
        except Exception:
            self.handleError(record)
    
    def _log_sender(self) -> None:
        """Background thread that processes the log queue and sends each log individually."""
        while not self.shutdown_event.is_set() or not self.log_queue.empty():
            try:
                # Get log entry with timeout
                try:
                    log_entry = self.log_queue.get(timeout=0.1)
                    
                    # Send individual log entry immediately
                    log_event = {
                        'timestamp': log_entry['timestamp'],
                        'message': json.dumps(log_entry)
                    }
                    
                    self._send_log(log_event)
                    self.log_queue.task_done()
                    
                except Empty:
                    pass
                    
            except Exception as e:
                print(f"Error in log sender: {e}")
    
    def _send_log(self, log_event: dict) -> None:
        """Send a single log event to CloudWatch."""
        try:
            kwargs = {
                'logGroupName': self.log_group,
                'logStreamName': self.log_stream,
                'logEvents': [log_event]
            }
            
            if self.sequence_token:
                kwargs['sequenceToken'] = self.sequence_token
                
            response = self.client.put_log_events(**kwargs)
            self.sequence_token = response['nextSequenceToken']
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidSequenceTokenException':
                self.sequence_token = e.response['Error']['Message'].split()[-1]
                self._send_log(log_event)  # Retry with correct sequence token
            else:
                raise
    
    def flush(self) -> None:
        """Wait for all logs in the queue to be processed."""
        self.log_queue.join()  # Block until all tasks are done

    def flush_and_stop(self) -> None:
        """Signal the worker to stop and wait for all logs to be sent."""
        if not self.shutdown_event.is_set():
            self.shutdown_event.set()
            try:
                # Wait for all remaining logs to be processed
                self.log_queue.join()
            except:
                pass
            
            if self.worker.is_alive():
                self.worker.join(timeout=2.0)  # Wait up to 2 seconds for worker to finish
    
    def close(self) -> None:
        """Clean up resources when shutting down."""
        self.flush_and_stop()
        super().close()