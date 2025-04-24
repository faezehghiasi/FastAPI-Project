from pydantic import  BaseModel


class Blog(BaseModel):
    title: str
    content: str
    author_id: int

    class Config:
        orm_mode = True


class ShowBlog(Blog):
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(User):
    class Config:
        orm_mode = True