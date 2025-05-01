from __future__ import annotations
from sqlmodel import SQLModel, Field, select
from typing import Optional
import uuid
from app.models import user_temp
from app.api.dependencies import database
from sqlmodel.ext.asyncio.session import AsyncSession  # if using async

class User(user_temp.BaseUser, table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        nullable=False
    )
    password_hash: str = Field(nullable=False)