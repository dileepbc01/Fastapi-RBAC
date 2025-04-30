from sqlmodel import SQLModel
from .user import User
from .project import Project
# Import any other models here

# This ensures all models are imported when the models package is imported
__all__ = ["User","Project"]  # Add other model names as needed