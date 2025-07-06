from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'rahul'}}

@app.get('/about')
def about(limit=10, published: bool = True, sort: Optional[str] = None):
    if published == True:
        return {'data':f'{limit} published blogs'}
    else:
        return {'data':f'{limit} unpublished blogs'}


@app.get('/about/unpublished')
def about():
    return { 'data': 'All the unpublished blogs' }

@app.get('/about/{id}')
def about(id:int):
    return { 'data': id }

@app.get('/about/{id}/comments')
def comments(id):
    return { 'data': '1'}

class Model1(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Model1):
    return {'data': f"Blog is created with title as {request.title}"}
