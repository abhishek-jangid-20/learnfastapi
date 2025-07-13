from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import models, schemas
from .. import database,hashing
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db:Session=Depends(get_db)):
    return user.createuser(request, db)

@router.post('/{id}',response_model=schemas.ShowUser)
def show(id, db:Session=Depends(get_db)):
    return user.showuser(id, db)