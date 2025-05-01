from typing import Annotated, AsyncGenerator
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.config import settings
from app.utils.enums import AppEnvironmentEnum
# PostgreSQL URL format

# Create an async engine for PostgreSQL
engine: AsyncEngine = create_async_engine(
    settings.database_url,
    echo=settings.env == AppEnvironmentEnum.DEVELOPMENT
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
