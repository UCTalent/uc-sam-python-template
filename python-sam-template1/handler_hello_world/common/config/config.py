from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from common.config.global_constants import separator_l1, len_separator_l3
import logging

logging.basicConfig(level=logging.NOTSET)
logging.getLogger()

GLOBAL_CONFIG = None


class Base(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    # App config
    API_ENV: str = Field(..., env='API_ENV', description='Environment for the API')
    API_KEY: SecretStr = Field(..., env='API_KEY', min_length=10, max_length=50,
                               description='API key for authentication')


if GLOBAL_CONFIG is None:
    GLOBAL_CONFIG = Base()
    logging.info(f"{separator_l1 * len_separator_l3}load config success!")
    logging.info(GLOBAL_CONFIG.json)
