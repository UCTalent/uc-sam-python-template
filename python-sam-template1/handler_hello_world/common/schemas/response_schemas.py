import json

from pydantic import BaseModel, Field
from enum import Enum


class EnumCode(int, Enum):
    """List of status code response """
    SUCCESS = 0
    ERROR = -1


class ResponseBodyBase(BaseModel):
    status: str = Field('ok')
    code: EnumCode = Field(EnumCode.SUCCESS.value)
    message: str = Field('')
    data: dict = Field({})
    raw_ai_prompt_message: str = Field('')
    raw_ai_response: str = Field('')


class ResponseBase(BaseModel):
    statusCode: int = Field(200)
    body: ResponseBodyBase = Field(ResponseBodyBase())
