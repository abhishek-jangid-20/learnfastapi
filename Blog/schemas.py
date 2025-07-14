from pydantic import BaseModel
from typing import List, Optional


class Model1(BaseModel):
    title: str
    body: str
    Id: int
    class cofi():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs : List[Model1] = []
    class cofi():
        orm_mode = True

    
class Showmodel(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class cofi():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Tokendata(BaseModel):
    email: Optional[str] = None