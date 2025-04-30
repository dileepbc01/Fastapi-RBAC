from sqlmodel import SQLModel, Field
from app.utils.enums import RoleEnum 


class BaseUser(SQLModel):
    username: str = Field(index=True, unique=True, nullable=False)
    role: RoleEnum = Field(default=RoleEnum.USER.value, nullable=False)

class UserCreate(BaseUser):
    password: str = Field(nullable=False)

