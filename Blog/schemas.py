from pydantic import BaseModel


class Model1(BaseModel):
    title: str
    body: str
    id: int
    
class Showmodel(BaseModel):
    title: str
    body: str
    class cofi():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str