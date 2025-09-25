import json
import traceback
from typing import Dict, Any
from uuid import uuid4

"""
THIS FUNCTION IS NOT YET IMPLEMENTED
"""

from services.aws.lambda_event_helper import LambdaEventHelper
from services.application.messages.mepcom_nlp_processing_messages import MEPCOMNLPProcessingMessages

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
            db_service = container.database_connection_service()
            # initialize other services
            # ...
            #s3_service = container.s3_service()
            #s3_service.
        except Exception as e:
            raise Exception(f"Error initializing services: {str(e)}") from e

        # safely extract the input data from the event body before validating
        variable_one = event.get("input_one", "")
        variable_two = event.get("input_two", "")
        

        # TODO: validate the input data

        with db_service.get_connection() as conn:
            # Using as_dict=True returns results as dictionaries, which is very convenient
            cursor = conn.cursor(as_dict=True)
            
            sql_query = "SELECT Id, Name, CreatedDate FROM dbo.DummyTable;"
            logger.info("Executing query", extra={"sql": sql_query})
            
            cursor.execute(sql_query)
            records = cursor.fetchall()
        
        logger.info(f"Successfully fetched {len(records)} records from the database.")


        # log the start of the process
        logger.info(MEPCOMNLPProcessingMessages.PROCESS_STARTED_MESSAGE, extra={
            "event_type": "process_start",
            "key_1": variable_one,
            "key_2": variable_two
        })


        # TODO: add implementation here


        logger.info(MEPCOMNLPProcessingMessages.PROCESS_COMPLETED_MESSAGE, extra={
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
        message = MEPCOMNLPProcessingMessages.INVALID_DATA_MESSAGE
        
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
        message = MEPCOMNLPProcessingMessages.GENERAL_ERROR_MESSAGE

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

