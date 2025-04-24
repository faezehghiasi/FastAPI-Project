from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db:Session , request: schemas.User):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog