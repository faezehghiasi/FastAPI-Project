from pydantic import  BaseModel
from typing import List

# ----------------- Input Schemas -----------------
class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    content: str


class Login(BaseModel):
    username : str
    password :str
     
# ----------------- Output Schemas -----------------

class ShowUser(BaseModel):
    name: str
    email: str
    blogs : List[Blog] = []
    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    author: ShowUser
    class Config:
        orm_mode = True
