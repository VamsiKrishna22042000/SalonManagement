from pydantic import BaseModel,EmailStr
import uuid
from typing import Optional

from enum import Enum


class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"
    staff = "staff"

class UserLoginP(BaseModel):
    email:EmailStr
    password:str

class UserP(BaseModel):
    name:str
    email:EmailStr
    password:str
    number:str
    address:Optional[str]=None
    role:RoleEnum
    salon_id:uuid.UUID

    class Config:

        from_attributes:True

class UserPResponse(UserP):
    id:uuid.UUID

    class Config:

        from_attributes:True
    