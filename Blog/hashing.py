from passlib.context import CryptContext
from . import schemas

pass_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class hash():
    def bcrypt(password: str):
        return pass_cxt.hash(password)
    
