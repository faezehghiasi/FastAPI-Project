from pydantic import  BaseModel
from typing import List
from typing import Optional

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
     

class Token(BaseModel):
    access_token :str
    token_type :str

class TokenDate(BaseModel):
    username : Optional[str] = None
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
