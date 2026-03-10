from pydantic_settings import BaseSettings, SettingsConfigDict
import os

from dotenv import load_dotenv

load_dotenv(override=True)

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_SERVER: str = "smtp.mail.ru"
    MAIL_PORT: int = 587
    MAIL_USE_TLS: bool = True
    gmail_user: str
    gmail_app_password: str
    SECRET_KEY: str

    URI: str | None = None
    URL_DATABASE: str | None = None

    def reload_env(self):
        load_dotenv(override=True)

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")
    SECRET_KEY: str

settings = Settings()
