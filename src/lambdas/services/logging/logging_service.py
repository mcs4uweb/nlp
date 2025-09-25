import logging
import sys
from typing import Optional, Dict, Any
from datetime import datetime

from services.logging.cloudwatch_handler import CloudWatchHandler


class LoggingService:
    """Custom logger class that handles both local and CloudWatch logging."""
    
    def __init__(
        self,
        cloudwatch_handler: CloudWatchHandler,
        service_name: str,
        log_level: int = logging.INFO,
        aws_region: Optional[str] = None,
        log_group: Optional[str] = None
    ):
        self.logger = logging.getLogger(service_name)
        self.logger.setLevel(log_level)
        
        # Prevent duplicate logs
        if self.logger.handlers:
            self.logger.handlers.clear()

        #self.logger.propagate = False
        
        # Set format
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Add console handler if a debugger is attached
        if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
        
        # Add CloudWatch handler if AWS configuration is provided
        if aws_region and log_group:
            cloudwatch_handler.setFormatter(formatter)
            self.logger.addHandler(cloudwatch_handler)
    
    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance."""
        return self.logger

    def flush_all_handlers(self) -> None:
        """
        Manually flush all handlers attached to the logger.
        
        This ensures that any buffered logs are immediately sent to their destinations,
        which is particularly useful before Lambda functions complete execution.
        """
        for handler in self.logger.handlers:
            try:
                handler.flush()
            except Exception as e:
                print(f"Error flushing handler {handler.__class__.__name__}: {str(e)}")