from common.config.config import GLOBAL_CONFIG
from common.schemas.response_schemas import ResponseBase
from common.utils.aws_lamda_helper import log_lamda_execution_info


def create_response():
    resp = ResponseBase()
    resp.body.message = 'hello world'
    resp.body.data = {
        "message": f"hello, this is sam python template env = {GLOBAL_CONFIG.API_ENV}",
    }
    return resp.dict()


def handler_hello_world(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    log_lamda_execution_info(context)
    return create_response()
