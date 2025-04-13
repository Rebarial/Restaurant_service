from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv(override=True)

class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    table: str = "/tables"
    reservation: str = "/reservations"

class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

class Settings(BaseSettings):

    api: ApiPrefix = ApiPrefix()
    
    DB_HOST: str 
    DB_PORT: int
    DB_USER: str 
    DB_PASSWORD: str 
    DB_NAME: str
    DB_CONTAINER: str
    DB_PORT2: int

    naming_conventions: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_CONTAINER}:{self.DB_PORT2}/{self.DB_NAME}"


    
    model_config = SettingsConfigDict(env_file=".env.app")
    
settings = Settings()
