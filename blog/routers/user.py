from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..repository import user
router = APIRouter(
    prefix='/users',
    tags=['UserS']
)


@router.get("/",response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(database.get_db)):
    user.get_users(db=db)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(db=db , request=request)




@router.get("/{id}",response_model=schemas.ShowUser)
def show(id: int, db: Session = Depends(database.get_db)):
    return user.get_user(id=id,db=db)