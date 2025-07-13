from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from .. import models, schemas
from .. import database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/{id}',status_code=200, response_model=schemas.Showmodel)
def all(id,response:Response, db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.Id == id).first()
    if not blogs:
        raise HTTPException(status_code=404, detail="Item not found")        
    return blogs

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Model1, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/')
def all(db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Yes Deleted'

@router.put('/{id}')
def upd(id,request: schemas.Model1, db : Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise  HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update({"title": request.title, "body": request.body}) # This line will raise an error
    db.commit()
    return 'Updated'