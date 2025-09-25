import boto3
from botocore.exceptions import ClientError
import json

class StepFunctionService:

    def __init__(self, region_name: str):
        self.region_name = region_name
        
        # Create a Secrets Manager client
        session = boto3.session.Session()
        self.client = session.client(
            service_name='stepfunctions',
            region_name=self.region_name
        )      

    def start(self, state_machine_arn, execution_input):

        response = self.client.start_execution(
            stateMachineArn=state_machine_arn,
            input=json.dumps(execution_input)
        )

        return response