from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ForEnvConfig(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class BotSettings(ForEnvConfig):
    """
    Settings of telegram bot
    """

    BOT_TOKEN: str = Field(..., description='Telegram bot token')


class RedisSettings(ForEnvConfig):
    REDIS_IP: str = Field(...)
    REDIS_PORT: int = Field(..., default=6379)
    REDIS_DATABASE: int = Field(..., default=0)
    REDIS_PASSWORD: str = Field(...)


class PostgresSettings(ForEnvConfig):
    POSTGRES_USER: str = Field(...)
    POSTGRES_PORT: int = Field(..., default=5432)
    POSTGRES_IP: str = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_DATABASE: str = Field(..., default='Main')


class ProjectStorage(BaseModel):
    """
    Here are stored data from all parts of this project
    """
    bot: BotSettings = BotSettings()
    redis: RedisSettings = RedisSettings()
    postgres: PostgresSettings = PostgresSettings()


transporter = ProjectStorage()
