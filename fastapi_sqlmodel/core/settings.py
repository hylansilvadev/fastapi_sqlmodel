from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_DEVELOPMENT: str
    DATABASE_DEVELOPMENT_ECHO: bool
    PROJECT_NAME: str
    PROJECT_VERSSION: str


settings = Settings()
