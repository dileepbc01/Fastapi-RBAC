from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class User(SQLModel,table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        nullable=False
    )    
    email: str = Field(index=True, unique=True, nullable=False)
    fullname: str = Field( nullable=False)
    password_hash: str = Field(nullable=False)
    role: str = Field(default="user", nullable=False)