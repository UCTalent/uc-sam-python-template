import logging

from common.config.config import GLOBAL_CONFIG
from common.config.global_constants import ENV_LOCAL

logging.basicConfig(level=logging.NOTSET)
logging.getLogger()


def log_lamda_execution_info(context):
    if GLOBAL_CONFIG.API_ENV == ENV_LOCAL:
        return
    logging.info("Lambda function ARN:", context.invoked_function_arn)
    logging.info("CloudWatch log stream name:", context.log_stream_name)
    logging.info("CloudWatch log group name:", context.log_group_name)
    logging.info("Lambda Request ID:", context.aws_request_id)
    logging.info("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    logging.info("Lambda time remaining in MS:", context.get_remaining_time_in_millis())
