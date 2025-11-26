from passlib.context import CryptContext
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")

from datetime import datetime,timezone,timedelta

from jose import jwt,JWTError,ExpiredSignatureError

import os

from dotenv import load_dotenv

load_dotenv()


SEC_KEY= os.getenv("SEC_KEY")
ALGO="HS256"
EXP=30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password:str,hashedPassword:str)->bool:
    return pwd_context.verify(password,hashedPassword)

def create_token(data:dict)->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXP)
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,SEC_KEY,algorithm=ALGO)




def validate_token(token:str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token,SEC_KEY,algorithms=[ALGO])

        return payload

    except ExpiredSignatureError:

        raise HTTPException(status_code=401,detail="Token Expired")
    
    except JWTError :

        raise HTTPException(status_code=401,detail="Un authorized User!")



def required_roles(*allowed_roles):
    def check_required_roles(payload:dict=Depends(validate_token)):

        role = payload.get("role")

        if role not in allowed_roles:

            raise HTTPException(status_code=403,detail="Forbidden insufficent role!")
        
        return payload
    return check_required_roles
