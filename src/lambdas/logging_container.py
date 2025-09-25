# minimal container just for logging
from datetime import datetime
import logging
from dependency_injector import containers, providers

from services.logging.logging_service import LoggingService
from services.logging.cloudwatch_handler import CloudWatchHandler


class LoggingContainer(containers.DeclarativeContainer):

    def set_configurations(config):
        config.aws_region_name.from_env("AWS_REGION_NAME", "us-gov-west-1")
        config.service_name.from_env("APPLICATION_NAME", "USMEPCOM-NLP-PROCESSOR")
        config.log_level.from_env("DEFAULT_LOG_LEVEL", logging.INFO)
        config.aws_log_group.from_env("AWS_LOG_GROUP", "/aws/lambda/awprmips-loggroup-mepcom-nlp-processor-dev")
        config.aws_log_stream.from_env("AWS_LOG_STREAM", f"{config.service_name()}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")

    main_container = None

    config = providers.Configuration()
    set_configurations(config)
    
    cloudwatch_handler = providers.Singleton(
        CloudWatchHandler,
        log_group=config.aws_log_group,
        log_stream=config.aws_log_stream,
        region_name=config.aws_region_name
    )

    logger = providers.Singleton(
        LoggingService,
        cloudwatch_handler=cloudwatch_handler,
        service_name=config.service_name,
        log_level=config.log_level,
        aws_region=config.aws_region_name,
        log_group=config.aws_log_group
    )

 