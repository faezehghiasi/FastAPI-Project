from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,database,models,token
from ..hashing import Hash


router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="username or password is incorrect")
    
    if not Hash.verify(hashed_password=user.password,plain_password=request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="username or password is incorrect")
    
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

