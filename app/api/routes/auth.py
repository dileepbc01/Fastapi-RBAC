from typing import Annotated
from fastapi import Depends
from app.api.dependencies.database import SessionDep 
from app.schemas.user import User
from fastapi import APIRouter, Depends
from sqlmodel import select
from app.models import user
from fastapi import HTTPException,status
from sqlmodel import select
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models.token import Token
from app.utils import create_acc_token, hash
from datetime import datetime,timedelta
from app.config import settings
from jwt.exceptions import InvalidTokenError
import jwt

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(db: SessionDep , token: str = Depends(oauth2_scheme), ) -> User:
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,settings.secret_key,algorithms=[settings.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    
    user = db.exec(select(User).where(User.username == username)).first()
    if user is None:
        raise credentials_exception
    return user




@router.post("/register")
async def register(user_data: user.UserCreate, db: SessionDep) -> None:
    existing_user = db.exec(select(User).where(User.username == user_data.username)).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = hash.get_password_hash(user_data.password)  # Replace with actual hashing logic
    
    new_user = User(username=user_data.username,role=user_data.role,password_hash=hashed_password)

    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
async def login_user(
       form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
       db:SessionDep
) -> Token:
    user_data= db.exec(select(User).where(User.username == form_data.username)).first()
    if not user_data:
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
def getMe(currentUser:User = Depends(get_current_user)):
    return currentUser