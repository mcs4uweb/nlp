import boto3
import time
from botocore.exceptions import ClientError
from typing import List, Dict, Any

class TextractService:
    """
    A service class for interacting with AWS Textract to extract text from documents,
    specifically handling the asynchronous workflow required for PDFs stored in S3.
    """

    def __init__(self, region_name: str, logger: Any, textract_s3_role_arn: str):
        """
        Initializes the service and the boto3 client for Textract.

        Args:
            region_name (str): The AWS region to use.
            logger (Any): An instance of a configured logger.
            textract_s3_role_arn (str): The ARN of the IAM Role that Textract can assume
                                        to access the S3 bucket.
        """
        self.region_name = region_name
        self.textract_s3_role_arn = textract_s3_role_arn
        self.client = boto3.client("textract", region_name=self.region_name)

    def process_pdf_from_s3(self, bucket_name: str, object_key: str) -> str:
        """
        Orchestrates the asynchronous processing of a PDF from S3.

        This method starts a Textract job, waits for it to complete, fetches all
        the results, and compiles them into a single string.

        Args:
            bucket_name (str): The S3 bucket where the PDF is located.
            object_key (str): The key (path) of the PDF file in the bucket.

        Returns:
            str: The full text content extracted from the PDF, with pages separated by newlines.
                 Returns an empty string if the process fails or no text is found.
        """
        try:
            job_id = self._start_text_detection_job(bucket_name, object_key)
            if not job_id:
                return ""

            if not self._wait_for_job_completion(job_id):
                return ""

            all_blocks = self._get_job_results(job_id)
            
            # Filter for text lines and join them together
            text_lines = [block['Text'] for block in all_blocks if block['BlockType'] == 'LINE']
            
            return '\n'.join(text_lines)

        except ClientError as e:
            #self.logger.error("A critical AWS error occurred during Textract processing.", extra={"error": str(e)})
            return ""
        except Exception as e:
            #self.logger.error("An unexpected error occurred during Textract processing.", extra={"error": str(e)})
            return ""

    def _start_text_detection_job(self, bucket_name: str, object_key: str) -> str:
        """Starts a Textract text detection job and returns the JobId."""
         
        response = self.client.start_document_text_detection(
            DocumentLocation={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': object_key
                }
            },
            NotificationChannel={
                'RoleArn': self.textract_s3_role_arn,
                'SNSTopicArn': '' # SNS is optional but recommended for production
            }
        )
        job_id = response['JobId']
         
        return job_id

    def _wait_for_job_completion(self, job_id: str, timeout_secs: int = 300, poll_interval_secs: int = 5) -> bool:
        """Polls the Textract API until the job is complete or times out."""
        
        start_time = time.time()
        while time.time() - start_time < timeout_secs:
            response = self.client.get_document_text_detection(JobId=job_id)
            status = response['JobStatus']
            self.logger.debug(f"Current job status: {status}", extra={"job_id": job_id})

            if status == 'SUCCEEDED':
                self.logger.info("Textract job succeeded.", extra={"job_id": job_id})
                return True
            elif status == 'FAILED':
                self.logger.error("Textract job failed.", extra={"job_id": job_id, "status_message": response.get('StatusMessage')})
                return False
            
            time.sleep(poll_interval_secs)
        
        
        return False

    def _get_job_results(self, job_id: str) -> List[Dict[str, Any]]:
        """Fetches all paginated results for a completed Textract job."""
         
        all_blocks = []
        next_token = None
        
        while True:
            kwargs = {'JobId': job_id}
            if next_token:
                kwargs['NextToken'] = next_token

            response = self.client.get_document_text_detection(**kwargs)
            all_blocks.extend(response.get('Blocks', []))
            
            next_token = response.get('NextToken')
            if not next_token:
                break
        
        return all_blocks