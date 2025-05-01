from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.utils.get_current_user import get_current_user
from app.api.dependencies.database import SessionDep
from app.schemas.user import User
from app.models import user
from app.models.token import Token
from app.utils import create_acc_token, hash
from app.config import settings

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register(
    user_data: user.UserCreate,
    db: SessionDep,
) -> dict:
    existing_user = await db.exec(select(User).where(User.username == user_data.username))
    existing_user = existing_user.first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = hash.get_password_hash(user_data.password)  # Replace with actual hashing logic

    new_user = User(username=user_data.username, role=user_data.role, password_hash=hashed_password)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
      db: SessionDep
) -> Token:
    user_data = await db.exec(select(User).where(User.username == form_data.username))
    user_data = user_data.first()

    if not user_data or not hash.verify_password(form_data.password, user_data.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_acc_token.create_access_token(
        data={"sub": user_data.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user