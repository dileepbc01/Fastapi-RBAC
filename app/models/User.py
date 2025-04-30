from sqlmodel import SQLModel, Field

class BaseUser(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False)
    role: str = Field(default="user", nullable=False)
    
class UserCreate(BaseUser):
    password:str = Field(index=True, unique=True, nullable=False)