# from fastapi import FastAPI
# from models import Base
# from database import engine
# from routers import search

# app = FastAPI()

# Base.metadata.create_all(bind=engine)

# app.include_router(search.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database import engine
from routers import book

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router)
