from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
import sys
import os
from dotenv import load_dotenv

load_dotenv()
# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import your SQLModel models and metadata
from sqlmodel import SQLModel
from app.schemas import Project, User  # Import all your models here

# this is the Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set SQLModel metadata for Alembic
target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )
    
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    """Run migrations in 'online' mode using async engine."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    
    await connectable.dispose()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Check if we're using an async database URL
    url = config.get_main_option("sqlalchemy.url")
    if url.startswith('postgresql+asyncpg') or url.startswith('sqlite+aiosqlite'):
        # For async databases, use async migrations
        import asyncio
        asyncio.run(run_async_migrations())
    else:
        # Traditional synchronous approach
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection, target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()