from passlib.context import CryptContext
from . import schemas

pass_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class hash():
    def bcrypt(password: str):
        return pass_cxt.hash(password)
    
    def verify(hashed_pass,plain_pass):
        return pass_cxt.verify(plain_pass, hashed_pass)

    
