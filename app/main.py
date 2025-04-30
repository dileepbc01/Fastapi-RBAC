import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI

import uvicorn


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
