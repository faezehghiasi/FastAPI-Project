from fastapi import FastAPI
from .database import engine
from . import models
from .routers import blogs, user


app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blogs.router)
app.include_router(user.router)