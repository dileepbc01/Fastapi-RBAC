from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

class Project(SQLModel,table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        nullable=False
    )
    name: str = Field( nullable=False)
    description: str = Field( nullable=False)