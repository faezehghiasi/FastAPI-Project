from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models ,oauth2
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

@router.get("/",response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user) ):
    return blog.create_blog(db=db, request=request, current_user=current_user)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(db=db,id=id)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(db=db,request=request,id=id)

@router.get("/{id}",response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(db=db,id=id)


