from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from ..hashing import Hash
from sqlalchemy.orm import Session
router = APIRouter()


@router.get("/users",response_model=List[schemas.ShowUser],tags=["Users"])
async def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser,tags=["Users"])
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email ,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/users/{id}",response_model=schemas.ShowUser,tags=["Users"])
def show(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user