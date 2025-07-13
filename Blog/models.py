from sqlalchemy import Column, Integer, String
from .database import base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Blog(base):
    __tablename__ = 'Blogs'
    Id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('Users.Id'))

    creator = relationship("User", back_populates="blogs")

class User(base):
    __tablename__ = 'Users'
    Id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")