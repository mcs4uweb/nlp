import json
import traceback
from typing import Dict, Any
from uuid import uuid4

"""
THIS FUNCTION IS NOT YET IMPLEMENTED
"""

from services.aws.lambda_event_helper import LambdaEventHelper
from services.application.messages.mepcom_nlp_post_processing_messages import MEPCOMNLPPostProcessingMessages

# inline DI container initialization needed for Lambda execution
from logging_container import LoggingContainer
logging_container = LoggingContainer()
from container import Container
container = Container()


def lambda_handler(event, context):

    # initialize variables for possible error handling
    variable_one = ""
    variable_two = ""
    
    try:

        try:
            # initialize logging service
            logger = logging_container.logger().get_logger()
            # initialize other services
            # ...
        except Exception as e:
            raise Exception(f"Error initializing services: {str(e)}") from e

        # safely extract the input data from the event body before validating
        variable_one = event.get("input_one", "")
        variable_two = event.get("input_two", "")
        

        # TODO: validate the input data


        # log the start of the process
        logger.info(MEPCOMNLPPostProcessingMessages.PROCESS_STARTED_MESSAGE, extra={
            "event_type": "process_start",
            "key_1": variable_one,
            "key_2": variable_two
        })


        # TODO: add implementation here


        logger.info(MEPCOMNLPPostProcessingMessages.PROCESS_COMPLETED_MESSAGE, extra={
            "event_type": "process_complete",
            "key_1": variable_one,
            "key_2": variable_two,
            "other_details": "additional details here"
        })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"ok",
                "key_1": variable_one,
                "key_2": variable_two
            }),
        }
    
    except ValueError as e:
        correlation_id = str(uuid4())
        error_message = str(e)
        message = MEPCOMNLPPostProcessingMessages.INVALID_DATA_MESSAGE
        
        logger.error(message, extra={
            "event_type": "validation_error",
            "error_message": error_message,
            "key_1": variable_one,
            "key_2": variable_two,
            "correlation_id": correlation_id
        })

        return {
            "statusCode": 400,
            "stopProcessing": True,
            "body": json.dumps({
                "message": error_message,
                "key_1": variable_one,
                "key_2": variable_two,
                "correlation_id": correlation_id
            })
        }
    
    except Exception as e:
        correlation_id = str(uuid4())
        error_message = str(e)
        stack_trace = traceback.format_exc()
        message = MEPCOMNLPPostProcessingMessages.GENERAL_ERROR_MESSAGE

        logger.error(message, extra={
            "event_type": "general_error",
            "error_message": error_message,
            "key_1": variable_one,
            "key_2": variable_two,
            "correlation_id": correlation_id,
            "stack": stack_trace
        })

        return {
            "statusCode": 500,
            "stopProcessing": True,
            "body": json.dumps({
                "message": error_message, 
                "key_1": variable_one,
                "key_2": variable_two,
                "correlation_id": correlation_id
            })
        }
    
    finally:
        # Ensure all handlers are flushed before exiting
        logging_container.logger().flush_all_handlers()

