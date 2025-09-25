import pymssql

from services.aws.secrets_manager_service import SecretsManagerService

class DatabaseConnectionService:

    def __init__(self, secrets_manager_service: SecretsManagerService, region_name: str, connection_secret_name: str):
        self.region_name = region_name
        self.connection_secret = secrets_manager_service.get_secret(connection_secret_name) # get into configuratrion

    def get_connection(self):

        conn = pymssql.connect(host=self.connection_secret["host"], 
            database=self.connection_secret["dbname"], 
            port=1433,
            user=self.connection_secret["username"],
            password=self.connection_secret["password"]
        )
        
        return conn