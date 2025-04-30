import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
import asyncpg

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from contextlib import asynccontextmanager
import asyncpg
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Establish the database connection
        app.state.db = await asyncpg.connect("postgresql://dev-user:password@postgres:5432/fastapi_rbac")
        print("Connected to the database!")
        yield
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e  # Re-raise the error if you want FastAPI to handle it (e.g., server shutdown)
    finally:
        # Ensure the database connection is closed in case of any errors
        if hasattr(app.state, 'db') and app.state.db:
            await app.state.db.close()
            print("Database connection closed!")


app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
