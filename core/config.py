from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = 'postgresql+asyncpg://postgres:123@localhost/Library'
    db_echo: bool = False

settings = Setting()
