from app.api.dependencies.database import SessionDep 
from app.schemas import Project
from app.schemas.project import ProjectCreate
from fastapi import APIRouter, Depends
from sqlmodel import select
router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get('/')
async def get_projects(
    db : SessionDep,
) -> list[Project]:
    projects = db.exec(select(Project)).all()
    return projects

@router.post('/')
async def create_project(
    projectCreate: ProjectCreate,
    db : SessionDep,
) -> Project:
    project = Project(**projectCreate.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project