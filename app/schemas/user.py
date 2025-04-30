from __future__ import annotations
from sqlmodel import SQLModel, Field, select
from typing import Optional
import uuid
from app.models import user
from app.api.dependencies import database
from sqlmodel.ext.asyncio.session import AsyncSession  # if using async

class User(user.BaseUser, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        nullable=False
    )
    password_hash: str = Field(nullable=False)
    
    # @staticmethod
    # def get_user_by_username(session: database.SessionDep, username: str) -> Optional[User]:
    #     existing_user= session.exec(select(User).where(User.username == username)).first()
    #     print("username",existing_user)
    #     return existing_user
