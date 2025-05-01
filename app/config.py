from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from app.utils.enums import LogLevelEnum, AppEnvironmentEnum
load_dotenv()  

class Settings(BaseSettings):
    database_url: str
    secret_key:str
    algorithm:str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI project"
    oauth_token_secret: str = "my_dev_secret"
    log_level: LogLevelEnum = LogLevelEnum.DEBUG
    access_token_expire_minutes:int=15
    env:AppEnvironmentEnum = AppEnvironmentEnum.DEVELOPMENT

settings = Settings()  # type: ignore
