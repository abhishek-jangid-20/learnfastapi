from pydantic import BaseModel


class Model1(BaseModel):
    title: str
    body: str
    id: int
    