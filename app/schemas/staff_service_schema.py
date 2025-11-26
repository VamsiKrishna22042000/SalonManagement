from pydantic import BaseModel,EmailStr

from typing import Optional,List

import uuid

class SalonP(BaseModel):
    name:str
    address:str
    city:Optional[str]=None
    pincode:Optional[str]
    country:str

    class Config:
            from_attributes=True
class SalonPResponse(SalonP):
      id:uuid.UUID

      class Config:
            from_attributes=True

class SerivceP(BaseModel):
    salon_id:uuid.UUID
    name:str
    price:float
    description:Optional[str]=None

    class Config:
            from_attributes=True

class SerivcePResponse(SerivceP):
      id:uuid.UUID

      class Config:
            from_attributes=True

class StaffP(BaseModel):

    salon_id:uuid.UUID
    name:str
    email:EmailStr
    expirence:int
    service_specality:List[str]
    rating:Optional[float]=0.0
    slots:List[str]=["9:00AM-10:00AM","10:00AM-11:00AM","11:00AM-12:00PM","12:00PM-1:00PM","1:00PM-2:00PM","2:00PM-3:00PM","3:00PM-4:00PM","4:00PM-5:00PM","5:00PM-6:00PM","6:00PM-7:00PM","7:00PM-8:00PM","8:00PM-9:00PM"]
    
    class Config:
            from_attributes=True

class StaffSPResponse(StaffP):
      id:uuid.UUID

      class Config:
            from_attributes=True



