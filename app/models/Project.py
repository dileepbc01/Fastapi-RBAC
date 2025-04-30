from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class ProjectCreate(SQLModel):
    name: str
    description: str



class Project(ProjectCreate,table=True):
    id: Optional[uuid.UUID] = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        nullable=False
    )
   