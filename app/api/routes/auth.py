from app.api.dependencies.database import SessionDep 
from app.models.user import User
from fastapi import APIRouter, Depends
from sqlmodel import select
router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.get("/register")
async def get_users(
    db : SessionDep,
) -> list[User]:
    users = db.exec(select(User)).all()
    return users



@router.get("/login")
async def get_users(
    db : SessionDep,
) -> list[User]:
    users = db.exec(select(User)).all()
    return users