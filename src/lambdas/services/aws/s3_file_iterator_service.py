from typing import Generator, Dict, Any

from .s3_service import S3Service

class S3FileIteratorService:
    """
    A service class that provides an efficient way to iterate over objects in an S3 bucket.
    It handles API pagination automatically, yielding one object at a time to conserve memory.
    """

    def __init__(self, s3_service: S3Service, logger: Any):
        """
        Initializes the service.

        Args:
            s3_service (S3Service): An instance of the S3Service to get a boto3 client.
            logger (Any): An instance of a configured logger.
        """
        self._s3_client = s3_service.s3_client  # Get the raw boto3 client from S3Service
        
    def iterate_objects(self, bucket_name: str, prefix: str = "", suffix: str = "") -> Generator[Dict[str, Any], None, None]:
        """
        A generator that yields S3 objects from a bucket, handling pagination.

        This is memory-efficient as it does not load the entire object list into memory.

        Args:
            bucket_name (str): The name of the S3 bucket.
            prefix (str, optional): Filters results to keys starting with this prefix (e.g., 'invoices/2023/'). Defaults to "".
            suffix (str, optional): Filters results to keys ending with this suffix (e.g., '.pdf'). Defaults to "".

        Yields:
            Generator[Dict[str, Any], None, None]: A dictionary for each S3 object found,
                                                   containing keys like 'Key', 'LastModified', 'Size', etc.
        """
        paginator = self._s3_client.get_paginator('list_objects_v2')
        
      
        object_count = 0
        try:
            # Create pages of 1000 objects at a time
            pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
            
            for page in pages:
                # The 'Contents' key may not exist if the prefix is empty
                for s3_object in page.get('Contents', []):
                    # Apply the suffix filter if one was provided
                    if suffix and not s3_object['Key'].endswith(suffix):
                        continue
                    
                    object_count += 1
                    yield s3_object # This is the core of the generator
        
        except Exception as e:
            """ self._logger.error(
                "Failed during S3 object iteration.",
                extra={"bucket": bucket_name, "prefix": prefix, "error": str(e)}
            ) """
            # Re-raise the exception to be handled by the caller
            raise

        """ self._logger.info(
            "Finished S3 object iteration.",
            extra={"bucket": bucket_name, "prefix": prefix, "total_objects_yielded": object_count}
        ) """

    def read_object_text(self, bucket_name: str, key: str, encoding: str = 'utf-8-sig') -> str:
        """
        Read an S3 object's content and decode to text.

        Args:
            bucket_name: The name of the S3 bucket.
            key: The object's key (path) in the bucket.
            encoding: Text encoding to decode with. Defaults to 'utf-8-sig' to strip BOM if present.

        Returns:
            The decoded text content of the object.
        """
        resp = self._s3_client.get_object(Bucket=bucket_name, Key=key)
        return resp['Body'].read().decode(encoding, errors='replace')
