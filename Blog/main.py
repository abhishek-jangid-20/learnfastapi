from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models,hashing
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




@app.post('/blog',status_code=status.HTTP_201_CREATED)
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

@app.get('/blog/{id}',status_code=200, response_model=schemas.Showmodel)
def all(id,response:Response, db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.Id == id).first()
    if not blogs:
        raise HTTPException(status_code=404, detail="Item not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'deatil': f'Blog with the id {id} is not available''}
    return blogs

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Yes Deleted'

@app.put('/blog/{id}')
def upd(id,request: schemas.Model1, db : Session=Depends(get_db)):
    # Error: blog.update() expects a dictionary of column values, not the request object directly
    # Should be: blog.update({"title": request.title, "body": request.body})
    blog = db.query(models.Blog).filter(models.Blog.Id==id)
    if not blog.first():
        raise  HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update({"title": request.title, "body": request.body}) # This line will raise an error
    db.commit()
    return 'Updated'



@app.post('/user')
def create_user(request : schemas.User, db:Session=Depends(get_db)):
    user = models.User(name=request.name, email=request.email, password=hashing.hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
