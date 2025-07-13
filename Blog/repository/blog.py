from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException, status


def all(id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.Id == id).first()
    if not blogs:
        raise HTTPException(status_code=404, detail="Item not found")        
    return blogs

def create(request: schemas.Model1, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Yes Deleted'

def update(id:int, request:schemas.Model1, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update({"title": request.title, "body": request.body}) # This line will raise an error
    db.commit()
    return 'Updated'
