import logging

from common.config.config import GLOBAL_CONFIG
from common.config.global_constants import ENV_LOCAL

logging.basicConfig(level=logging.NOTSET)
logging.getLogger()


def log_lamda_execution_info(context):
    if GLOBAL_CONFIG.API_ENV == ENV_LOCAL:
        return
    # logging.info(f"Lambda function ARN: {context.invoked_function_arn}")
    # logging.info(f"CloudWatch log stream name: {context.log_stream_name}")
    logging.info(f"CloudWatch log group name: {context.log_group_name}")
    logging.info(f"Lambda Request ID: {context.aws_request_id}")
    # logging.info(f"Lambda function memory limits in MB: {context.memory_limit_in_mb}")
    # logging.info(f"Lambda time remaining in MS: {context.get_remaining_time_in_millis()}")
