from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from ..hashing import Hash
from sqlalchemy.orm import Session


def get_users(db:Session):
    users = db.query(models.User).all()
    return users


def create_user(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email ,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

