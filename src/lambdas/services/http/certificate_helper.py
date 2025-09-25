import tempfile
from typing import Tuple
from services.aws.secrets_manager_service import SecretsManagerService


class CertificateHelper:

    def __init__(self, sm_service: SecretsManagerService) -> None:
        self.sm_service = sm_service

    def get_certificate(self, cert_secret_path: str, key_secret_path: str) -> Tuple[str, str]:
        mepcom_cert = self.sm_service.get_secret(cert_secret_path, deserialize=False)
        private_key = self.sm_service.get_secret(key_secret_path, deserialize=False)

        # Create a temporary PEM file with the mepcom cert
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pem', delete=False) as temp_cert_pem:
            temp_cert_pem.write(mepcom_cert)
            temp_cert_pem_path = temp_cert_pem.name

        # Create a temporary PEM file with the private key
        with tempfile.NamedTemporaryFile(mode='w', suffix='.key', delete=False) as temp_pk_pem:
            temp_pk_pem.write(private_key)
            temp_pk_pem_path = temp_pk_pem.name

        return (temp_cert_pem_path, temp_pk_pem_path)