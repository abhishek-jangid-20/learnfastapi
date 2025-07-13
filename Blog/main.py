from fastapi import FastAPI
from . import models
from .database import engine
from .routers import Blog , User

app = FastAPI()

models.base.metadata.create_all(bind=engine)

app.include_router(Blog.router)
app.include_router(User.router)

