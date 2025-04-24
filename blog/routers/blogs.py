from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/blogs",response_model=List[schemas.ShowBlog],tags=["Blogs"])
async def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post("/blogs",status_code=status.HTTP_201_CREATED,tags=["Blogs"])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
   
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete("/blogs/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def delete(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


@router.put("/blogs/{id}",status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update(request)
    db.commit()
    return {"message": "Blog updated successfully"}


@router.get("/blogs/{id}",response_model=schemas.ShowBlog,tags=["Blogs"])
def show(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog



