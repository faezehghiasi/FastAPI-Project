from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status,HTTPException


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db:Session , request: schemas.User):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blog(db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}