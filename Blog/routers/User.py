from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import models, schemas
from .. import database,hashing
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db:Session=Depends(get_db)):
    user = models.User(name=request.name, email=request.email, password=hashing.hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post('/{id}',response_model=schemas.ShowUser)
def show(id, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.Id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    return user