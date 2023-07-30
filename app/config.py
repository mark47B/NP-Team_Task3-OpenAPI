from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PRJ_TITLE: str
    PRJ_VERSION: str
    PRJ_DEBUG_ENVIRONMENT: bool

    SERVICE_ACCOUNT_CREDENTIALS_PATH: str
    SPREADSHEET_ID: str

    class Config:
        env_file = "../config/debug.env"
        env_file_encoding = "utf-8"


config = Settings()
