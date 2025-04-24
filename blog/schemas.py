from pydantic import  BaseModel


# ----------------- Input Schemas -----------------
class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    content: str



# ----------------- Output Schemas -----------------

class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    author: ShowUser
    class Config:
        orm_mode = True
