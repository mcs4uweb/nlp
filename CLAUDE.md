# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the USMEPCOM MIRS NLP Processor project - an AWS Serverless application that processes medical notes using AWS Comprehend Medical for natural language processing. The project uses AWS SAM (Serverless Application Model) for deployment and consists of Lambda functions orchestrated by Step Functions.

## Architecture

### Core Components

1. **Lambda Functions** (src/lambdas/):
   - `mepcom_sql_get_job_state.py` - Retrieves job state from SQL database
   - `mepcom_note_harvest.py` - Harvests medical notes for processing
   - `mepcom_acm_invoke_sync.py` - Invokes AWS Comprehend Medical synchronously
   - `mepcom_postprocess_counts.py` - Post-processes PDC counts
   - `mepcom_sql_set_job_state.py` - Updates job state in SQL database

2. **Step Function Pipeline**: Orchestrates the Lambda functions in sequence:
   Get Job State → Note Harvest → ACM Invoke → Post Process → Set Job State

3. **Service Layer** (src/lambdas/services/):
   - AWS services (S3, Comprehend Medical, Secrets Manager, Step Functions, Textract)
   - SQL Server integration via pymssql
   - HTTP/request handling with certificate support
   - Logging services with CloudWatch integration

4. **Dependency Injection**: Uses `dependency-injector` library with containers:
   - `container.py` - Main DI container for services
   - `logging_container.py` - Logging-specific container

## Development Commands

### Environment Setup
```bash
# Create and activate virtual environment (Windows)
python -m venv .venv
.venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt
```

### Build and Deploy
```bash
# Build the SAM application
sam build

# Deploy with guided prompts
sam deploy -g

# Deploy with existing configuration
sam deploy
```

### Testing
```bash
# Run tests with pytest (installed via requirements.txt)
pytest

# Run specific test file
pytest tests/unit/lambdas/test_specific.py

# Run with coverage
pytest --cov=src
```

## Environment Configuration

The application uses environment variables configured in `template.yaml`:
- `AWS_REGION_NAME`: us-gov-west-1
- `ENVIRONMENT`: dev/test/stg/prod
- `DB_CONNECTION_SECRET_NAME`: AWS Secrets Manager secret for database
- `ACM_ENDPOINT_URL`: Comprehend Medical FIPS endpoint
- `RESULTS_BUCKET`: S3 bucket for processing results
- `CONFIG_BUCKET`: S3 bucket for configuration

## Key Dependencies

- boto3: AWS SDK
- pymssql: SQL Server connectivity
- dependency-injector: Dependency injection framework
- pytest & pytest-mock: Testing framework
- requests: HTTP client
- dacite: Data class support

## Development Notes

- All Lambda functions follow a consistent error handling pattern with try-catch blocks
- Logging is centralized through the LoggingContainer
- Database connections are managed through DatabaseConnectionService using AWS Secrets Manager
- The application is designed to run in AWS GovCloud (us-gov-west-1)
- Lambda functions are configured with VPC access for database connectivity
- Each Lambda uses Lambda Layers for shared dependencies (imported from CloudFormation exports)