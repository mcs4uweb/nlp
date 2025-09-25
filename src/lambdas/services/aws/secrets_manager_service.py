import boto3
from botocore.exceptions import ClientError
import json

class SecretsManagerService:

    def __init__(self, region_name: str):
        self.region_name = region_name
        
        # Create a Secrets Manager client
        session = boto3.session.Session()
        self.client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )        

    def get_secret(self, secret_name, deserialize=True):

        # TODO: we will not need this statement in production
        # Set a default secret name if none is provided
        secret_name = secret_name or "digin/mssql/jcaban"

        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            raise e

        if deserialize:
            secret = json.loads(get_secret_value_response['SecretString'])
        else:
            secret = get_secret_value_response['SecretString']
                                               
        return secret