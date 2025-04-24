from pydantic import  BaseModel


class Blog(BaseModel):
    title: str
    content: str
    author_id: int

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True