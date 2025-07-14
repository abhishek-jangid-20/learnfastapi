from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from .. import models, schemas
from .. import database
from sqlalchemy.orm import Session
from ..repository import blog
from . import oauth

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/{id}',status_code=200, response_model=schemas.Showmodel)
def withid(id,response:Response, db: Session=Depends(get_db)):
    return blog.all(id, db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Model1, db : Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/')
def all(db: Session=Depends(get_db),get_current_user:schemas.User = Depends(oauth.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}')    
def upd(id,request: schemas.Model1, db : Session=Depends(get_db)):
    return blog.update(id, request, db)