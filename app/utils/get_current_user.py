from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
import jwt
from jwt import InvalidTokenError
from app.schemas import User
from sqlmodel import select
from app.config import settings
from app.api.dependencies.database import SessionDep 
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from api.dependencies.database import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    db:SessionDep, token: str = Depends(oauth2_scheme), ) -> User:
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
    
    user = (await db.exec(select(User).where(User.username == username))).first()
    if user is None:
        raise credentials_exception
    return user