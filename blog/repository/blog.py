from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status,HTTPException


def get_all_blogs(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db:Session , request: schemas.Blog,current_user: models.User):
    new_blog = models.Blog(
        title=request.title,
        content=request.content,
        author_id=current_user.id  
    )
    db.add(new_blog)      
    db.commit()            
    db.refresh(new_blog)   
    return new_blog



def delete_blog(id : int ,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}

def update_blog(id:int,db:Session , request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update(request.model_dump())
    db.commit()
    return {"message": "Blog updated successfully"}

def get_blog(db:Session,id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog

