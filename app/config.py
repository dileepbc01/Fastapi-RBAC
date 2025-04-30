from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  

class Settings(BaseSettings):
    database_url: str
    secret_key:str
    algorithm:str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI project"
    oauth_token_secret: str = "my_dev_secret"
    log_level: str = "DEBUG"
    access_token_expire_minutes:int=15


settings = Settings()  # type: ignore
