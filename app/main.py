import logging
import sys
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from app.api import routes 

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # Ensure proper context management

app = FastAPI(lifespan=lifespan)

app.include_router(routes.auth.router)
app.include_router(routes.projects.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
