from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix='/blogs',
    tags=['BlogS']
)

@router.get("/",response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all_blogs(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_blog(db,request)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db)):
    return blog.delete_blog(db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update_blog(db,request)

@router.get("/{id}",response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog.get_blog(db)


