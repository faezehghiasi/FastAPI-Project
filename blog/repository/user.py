from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas , database ,models
from ..hashing import Hash
from sqlalchemy.orm import Session


def get_users(db:Session):
    users = db.query(models.User).all()
    return users


