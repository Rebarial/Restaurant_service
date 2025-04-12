import sys
import os

sys.path = ['', '..'] + sys.path[1:]
sys.path.append(os.getcwd()+"\\app")
sys.path.append(os.getcwd()+"/app")

from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from api import router as api_router
from config import settings
from app.models import db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    await db_helper.dispose()

app = FastAPI(
    lifespan=lifespan
)

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)