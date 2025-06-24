import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

__AUTHOR__ = "Alocados Backend"
__VERSION__ = "0.1.0"

APP_NAME = "slackbot-boilerplate"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Settings(BaseSettings):
    # Description settings
    app_name: str = APP_NAME
    description: str = "Welcome to slackbot-boilerplate."
    term_of_service: str = "https://github.com/team-alocados/slackbot-boilerplate"
    contact_name: str = __AUTHOR__
    contact_url: str = "https://github.com/team-alocados/slackbot-boilerplate"
    contact_email: str = "develop@alocados.io"
    # Documentation url
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    # JWT settings
    jwt_secret_key: str = "super-secret"
    jwt_algorithm: str = "HS256"
    jwt_access_expires: int = 3600 * 24 * 7
    jwt_refresh_expires: int = 3600 * 24 * 30
    # Slow API settings
    slow_api_time: float = 0.5

    environment: str = "local"

    error_log_webhook: str

    slack_signing_secret: str

    slack_client_id: str
    slack_client_secret: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR + '/.env',
        env_file_encoding='utf-8',
    )


class TestSettings(Settings):
    """Test settings"""
    slow_api_time: float = 1.0
