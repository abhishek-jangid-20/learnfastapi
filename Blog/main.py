from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

models.base.metadata.create_all(bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()




@app.post('/blog')
def create_blog(request: schemas.Model1, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def all(id, db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.Id == id).first()
    return blogs
