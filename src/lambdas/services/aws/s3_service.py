import base64
import io
import time
import zipfile
import xml.etree.ElementTree as ET
from typing import BinaryIO, Optional, Union, List, Dict, Any
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import json

BEDROCK_CHAT_MODEL_ID = "amazon.nova-pro-v1:0"

WORD_MAIN_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

class S3Service:
    def __init__(self, region_name: str):
        self.region_name = region_name

        # Create an S3 client
        session = boto3.session.Session()
        self.s3_client = session.client(
            service_name='s3',
            region_name=self.region_name
        )  
        # Lazily created when Textract is used
        self._textract = None


    def bedrock_chat(self, system_prompt: str, user_prompt: str, model_id: str = BEDROCK_CHAT_MODEL_ID, max_tokens: int = 800, temperature: float = 0.3, top_p: float = 0.9, top_k: int | None = 20):
        
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name=self.region_name,
        )

        body = {
            "schemaVersion": "messages-v1",
            "system": [{"text": system_prompt}],
            "messages": [{"role": "user", "content": [{"text": user_prompt}]}],
            "inferenceConfig": {"maxTokens": max_tokens, "temperature": temperature, "topP": top_p},
        }
        if top_k is not None:
            body["inferenceConfig"]["topK"] = top_k
        resp = bedrock.invoke_model(modelId=model_id, body=json.dumps(body))
        out = json.loads(resp["body"].read())
        try:
            return out["output"]["message"]["content"][0]["text"]
        except Exception:
            return out
            return out

    def store_file(self, bucket_name: str, key: str, 
            body: Union[bytes, str, BinaryIO],
            content_type: Optional[str] = None,
            metadata: Optional[dict] = None
        ) -> str:
        """
        Upload an object to an S3 bucket.

        Args:
            bucket_name (str): Name of the target S3 bucket
            key (str): The object key (path) in the bucket
            body (Union[bytes, str, BinaryIO]): The object data to upload
            content_type (Optional[str]): The content type of the object
            metadata (Optional[dict]): Optional metadata dictionary

        Returns:
            str: The S3 URI of the uploaded object

        Raises:
            NoCredentialsError: If AWS credentials are not found
            Exception: For other AWS-related errors
        """
        try:
            # Prepare the upload parameters
            upload_args = {
                'Bucket': bucket_name,
                'Key': key,
                'Body': body
            }

            # Add optional parameters if provided
            if content_type:
                upload_args['ContentType'] = content_type
            if metadata:
                upload_args['Metadata'] = metadata

            # Upload the object
            self.s3_client.put_object(**upload_args)
            
            return f"s3://{bucket_name}/{key}"
            
        except NoCredentialsError:
            raise NoCredentialsError('AWS credentials not found')
        except Exception as e:
            raise Exception(f'Error uploading object to S3: {str(e)}')

    def move_file(self, source_bucket, source_key, destination_bucket, destination_key):
        # Copy the file from the source bucket to the destination bucket
        self.s3_client.copy_object(
            CopySource={'Bucket': source_bucket, 'Key': source_key},
            Bucket=destination_bucket,
            Key=destination_key
        )

        self.delete_file(source_bucket, source_key)

    def delete_file(self, source_bucket, source_key):
        # Delete the file from the source bucket
        self.s3_client.delete_object(Bucket=source_bucket, Key=source_key)

    def get_object_bytes(self, bucket_name: str, key: str) -> bytes:
        """
        Read an object's raw bytes from S3.

        Args:
            bucket_name: S3 bucket name
            key: S3 object key

        Returns:
            bytes: Raw object content
        """
        try:
            resp = self.s3_client.get_object(Bucket=bucket_name, Key=key)
            return resp["Body"].read()
        except NoCredentialsError:
            raise NoCredentialsError('AWS credentials not found')
        except Exception as e:
            raise Exception(f'Error reading object from S3: s3://{bucket_name}/{key} -> {str(e)}')

    def get_object_text(self, bucket_name: str, key: str, encoding: str = 'utf-8-sig') -> str:
        """
        Read an object's content from S3 and decode to text.

        Uses 'utf-8-sig' by default to gracefully strip a UTF-8 BOM if present.

        Args:
            bucket_name: S3 bucket name
            key: S3 object key
            encoding: Text encoding to use for decoding (default 'utf-8-sig')

        Returns:
            str: Decoded text content
        """
        data = self.get_object_bytes(bucket_name, key)
        return data.decode(encoding, errors='replace')


    def get_word_document_text(self, bucket_name: str, key: str) -> str:
        """
        Read a DOCX Word document from S3 and return its plain-text content.

        Args:
            bucket_name: S3 bucket name
            key: S3 object key referencing a .docx file

        Returns:
            Extracted document text. Returns an empty string when the document
            cannot be parsed.
        """
        doc_bytes = self.get_object_bytes(bucket_name, key)
        return self._extract_docx_text(doc_bytes)

    @staticmethod
    def _extract_docx_text(docx_bytes: bytes) -> str:
        """Convert DOCX binary content into plain text."""
        if not docx_bytes:
            return ""

        try:
            with zipfile.ZipFile(io.BytesIO(docx_bytes)) as docx_zip:
                document_xml = docx_zip.read('word/document.xml')
        except (zipfile.BadZipFile, KeyError):
            return ""

        try:
            root = ET.fromstring(document_xml)
        except ET.ParseError:
            return ""

        paragraph_tag = f"{WORD_MAIN_NAMESPACE}p"
        text_tag = f"{WORD_MAIN_NAMESPACE}t"
        tab_tag = f"{WORD_MAIN_NAMESPACE}tab"
        break_tags = {f"{WORD_MAIN_NAMESPACE}br", f"{WORD_MAIN_NAMESPACE}cr"}

        paragraphs: List[str] = []
        for paragraph in root.iter(paragraph_tag):
            parts: List[str] = []
            for node in paragraph.iter():
                if node.tag == text_tag:
                    if node.text:
                        parts.append(node.text)
                elif node.tag == tab_tag:
                    parts.append('	')
                elif node.tag in break_tags:
                    parts.append('')
            if parts:
                paragraph_text = ''.join(parts).replace('', '')
                paragraphs.append(paragraph_text)

        return ''.join(paragraphs).strip()

    def decode_and_store_file(self, encoded_file, file_type, bucket_name, s3_key):

        # Check if the file type is supported
        if file_type not in ['pdf', 'docx', 'doc']:
            raise ValueError('Unsupported file type. Only PDF, DOCX, and DOC files are supported.')
        
        # Get content type based on file type from switch case
        content_type = {
            'pdf': 'application/pdf',
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'doc': 'application/msword'
        }[file_type]

        try:
            # Decode the base64-encoded file
            decoded_file = base64.b64decode(encoded_file)

            return decoded_file

            # Upload the file to the specified S3 bucket
            #self.s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=decoded_file, ContentType=content_type)
            return self.store_file(
                bucket_name=bucket_name, key=s3_key,
                body=decoded_file, content_type=content_type
            )
        except NoCredentialsError:
            print('Credentials not available.')
        except Exception as e:
            print(f'An error occurred: {e}')

    # -----------------------------
    # Textract helpers for PDFs
    # -----------------------------
    def _get_textract_client(self):
        """Get or create a boto3 Textract client bound to this region."""
        if self._textract is None:
            self._textract = boto3.client('textract', region_name=self.region_name)
        return self._textract

    def extract_text_from_pdf(self, bucket_name: str, key: str, timeout_secs: int = 300, poll_interval_secs: int = 1) -> str:
        """
        Use AWS Textract to extract text from a PDF stored in S3.

        This starts an asynchronous job with Textract and polls until completion,
        then returns concatenated text lines.

        Args:
            bucket_name: Source S3 bucket
            key: PDF object key in S3
            timeout_secs: Max seconds to wait for job completion
            poll_interval_secs: Seconds between status polls

        Returns:
            Extracted text content as a single string. Returns empty string on failure.
        """
        try:
            client = self._get_textract_client()
            start_resp = client.start_document_text_detection(
                DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': key}}
            )
            job_id = start_resp['JobId']

            # Poll for completion
            start_time = time.time()
            while time.time() - start_time < timeout_secs:
                status_resp = client.get_document_text_detection(JobId=job_id)
                status = status_resp.get('JobStatus')
                if status == 'SUCCEEDED':
                    break
                if status == 'FAILED':
                    return ""
                time.sleep(poll_interval_secs)
            else:
                # Timed out
                return ""

            # Collect all paginated results
            all_blocks: List[Dict[str, Any]] = []
            next_token: Optional[str] = None
            while True:
                kwargs: Dict[str, Any] = {'JobId': job_id}
                if next_token:
                    kwargs['NextToken'] = next_token
                page = client.get_document_text_detection(**kwargs)
                all_blocks.extend(page.get('Blocks', []))
                next_token = page.get('NextToken')
                if not next_token:
                    break

            # Extract text lines
            lines = [b['Text'] for b in all_blocks if b.get('BlockType') == 'LINE' and 'Text' in b]
            return "\n".join(lines)

        except (ClientError, NoCredentialsError):
            return ""
        except Exception:
            return ""

    def upload_pdf_and_extract_text(self, bucket_name: str, key: str, pdf_bytes: bytes) -> str:
        """
        Convenience method: upload a PDF's bytes to S3 then extract text via Textract.

        Args:
            bucket_name: Target S3 bucket
            key: Destination key for the PDF
            pdf_bytes: Raw PDF bytes

        Returns:
            Extracted text content as a single string, or empty string on failure.
        """
        self.store_file(bucket_name, key, pdf_bytes, content_type='application/pdf')
        return self.extract_text_from_pdf(bucket_name, key)


# local testing
if __name__ == "__main__":
    pass
