from .. import models
from sqlalchemy.orm import Session
from .. import hashing,schemas
from fastapi import HTTPException, status

def createuser(request: schemas.User, db:Session):
    user = models.User(name=request.name, email=request.email, password=hashing.hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def showuser(id:int, db:Session):
    user = db.query(models.User).filter(models.User.Id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user