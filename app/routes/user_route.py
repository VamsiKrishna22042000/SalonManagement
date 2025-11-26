from fastapi import APIRouter,Depends,HTTPException

from ..config.db_connection import get_session
from sqlalchemy.orm import Session

from ..schemas.user_schema import UserP,UserLoginP
from ..models.user_model import User
from ..models.staff_service_model import Salon

from ..config.auth import hash_password,create_token,verify_password,validate_token,required_roles

user_router = APIRouter(prefix="",tags=["Users"])


@user_router.post("/register")
def register_user(user:UserP,db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == user.salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon does not exist!")


    check_user = db.query(User).filter(User.email == user.email).first()

    if check_user:

        raise HTTPException(status_code=400,detail="User already exists!")
    
    hashed_password = hash_password(user.password)

    user_data = user.model_dump()
    user_data["password"] = hashed_password
    
    user_created = User(**user_data)
    
    db.add(user_created)

    db.commit()

    db.refresh(user_created)

    return {"status":200,"message":"User created successfully","data":user_created}


@user_router.post("/login")
def login_user(user:UserLoginP,db:Session=Depends(get_session)):

    check_user:UserP = db.query(User).filter(User.email==user.email).first()
    
    if not check_user:

        raise HTTPException(status_code=400,detail="User does not exists!")
    
    check_password = verify_password(user.password,check_user.password)

    if not check_password:

        raise HTTPException(status_code=400,detail="In correct password!")
    
    payload = {
        "name":check_user.name,
        "email":check_user.email 
    }
    
    token = create_token(payload)
    
    return {"status":200,"message":"User logged in successfully","token":token}

@user_router.put("/user/{id}/{salon_id}")
def edit_user(id:str,user:UserP,salon_id:str,payload:dict=Depends(required_roles("admin","user")),db:Session=Depends(get_session)):

    check_user = db.query(User).filter(User.salon_id==salon_id,User.id == id).first()

    if not check_user:

        raise HTTPException(status_code=400,detail="User does not exist!")
    
    edited_user = user.model_dump(exclude_unset=True)

    for field,value in edited_user.items():
        setattr(check_user,field,value)
    
    db.commit()
    db.refresh(check_user)

    return {"status":400,"message":"User updated Succesfully","data":check_user}


@user_router.delete("/user/{id}/{salon_id}")
def delet_user(id:str,salon_id:str,payload:dict=Depends(required_roles("admin","user")),db:Session=Depends(get_session)):
     
    check_user = db.query(User).filter(User.salon_id==salon_id,User.id == id).first()

    if not check_user:

        raise HTTPException(status_code=400,detail="User does not exists!")
    
    db.delete(check_user)

    db.commit()

    return {"status":200,"message":"User deleted successfully"}