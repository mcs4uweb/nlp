from datetime import datetime
from dependency_injector import containers, providers

# declare external logging container dependency
from logging_container import LoggingContainer
logging_container = LoggingContainer()

from services.application.repeat_function_with_delay import RepeatFunctionWithDelay
from services.http.request_helper import RequestHelper
from services.http.certificate_helper import CertificateHelper

from services.aws.secrets_manager_service import SecretsManagerService
from services.aws.step_function_service import StepFunctionService
from services.aws.s3_service import S3Service
from services.aws.comprehend_medical_service import ComprehendMedicalService
from services.aws.s3_file_iterator_service import S3FileIteratorService
from services.aws.textract_service import TextractService
from services.sqlserver.database_connection_service import DatabaseConnectionService
from services.sqlserver.database_repository import DatabaseRepository
from services.sqlserver.reporting_repository import ReportingRepository
from services.application.condition_scoring_service import ConditionScoringService
from services.application.clinical_report_service import ClinicalReportService

class Container(containers.DeclarativeContainer):
    
    def set_configurations(config):
        config.service_name.from_env("APPLICATION_NAME", "USMEPCOM-NLP-PROCESSOR")
        config.aws_region_name.from_env("AWS_REGION_NAME", "us-gov-west-1")
        config.pdf_s3_bucket.from_env("PDF_S3_BUCKET", "digin-di-testing")
        config.db_connection_secret_name.from_env("DB_CONNECTION_SECRET_NAME", "dev/mepcom/mssql/connection")

        
    config = providers.Configuration()
    set_configurations(config)

    logging_service = providers.Callable(
        lambda: logging_container.logger()
    )


    ## Application Services
    function_repeater = providers.Factory(
        RepeatFunctionWithDelay
    )

    ## AWS Services
    s3_service = providers.Singleton(
        S3Service,
        region_name=config.aws_region_name
    )
    
    secrets_manager_service = providers.Singleton(
        SecretsManagerService,
        region_name=config.aws_region_name
    )

    step_function_service = providers.Singleton(
        StepFunctionService,
        region_name=config.aws_region_name
    )

    ## helper services
    request_helper = providers.Singleton(
        RequestHelper
    )

    certificate_helper = providers.Singleton(
        CertificateHelper,
        sm_service=secrets_manager_service
    )
    
    condition_scoring_service = providers.Singleton(
        ConditionScoringService
    )

    clinical_report_service = providers.Singleton(
        ClinicalReportService
    )

    ## SQL Server Services
    database_connection_service = providers.Singleton(
        DatabaseConnectionService,
        secrets_manager_service=secrets_manager_service,
        region_name=config.aws_region_name,
        connection_secret_name=config.db_connection_secret_name
    )

    persons_table_repository = providers.Factory(
        DatabaseRepository,
        db_service=database_connection_service,
        
        primary_key_column="Id"      
    )

    reporting_repository = providers.Factory(
        ReportingRepository,
        db_service=database_connection_service
    )

    condition_scoring_service = providers.Singleton(
        ConditionScoringService
    )

    comprehend_medical_service = providers.Singleton(
        ComprehendMedicalService,
        region_name=config.aws_region_name,
        logger=logging_service,
        scoring_service=condition_scoring_service
    )

    s3_file_iterator_service = providers.Singleton(
        S3FileIteratorService,
        s3_service=s3_service,
        logger=logging_service  # Re-use the injected logger
    )

    textract_service = providers.Singleton(
        TextractService,
        region_name=config.aws_region_name,
        logger=logging_service,
        textract_s3_role_arn=config.textract_s3_role_arn
    )


