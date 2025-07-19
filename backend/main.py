from fastapi import FastAPI
from models import Base
from database import engine
from routers import search

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(search.router)
