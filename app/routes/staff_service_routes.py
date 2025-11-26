from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session

from ..config.db_connection import get_session
from ..schemas.staff_service_schema import SerivceP,StaffP
from ..models.staff_service_model import Salon,Service,Staff

from ..config.auth import validate_token,required_roles

staff_service_router = APIRouter(prefix="",tags=["Staffs","Services"])


#Service api's
@staff_service_router.post("/service")
def create_service(service:SerivceP,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == service.salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail=f"No salon with id {service.salon_id}!")
    
    check_service = db.query(Service).filter(Service.name == service.name).first()

    if check_service:

        raise HTTPException(status_code=400,detail=f"{service.name} already exists!")
    
    add_service = Service(**service.model_dump())
    
    db.add(add_service)

    db.commit()

    db.refresh(add_service)

    return {"status":200,"message":f"{service.name} added successfully","data":service}

@staff_service_router.get("/service/{salon_id}")
def get_services(salon_id:str,skip:int=Query(0,ge=0),limit:int=Query(0,ge=0),payload:dict=Depends(validate_token),db:Session=Depends(get_session)):
   
   check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

   if not check_salon:
       
       raise HTTPException(status_code=400,detail="Salon does not exist!")
   
   query = db.query(Service).filter(Service.salon_id == salon_id)
   
   if limit > 0:
       
       query = query.offset(skip).limit(limit)
   
   all_services = query.all()

   if not all_services:
      
      raise HTTPException(status_code=400,detail="No Services available")
   
   return {"status":200,"message":"Services successfully fetced", "data": all_services}

@staff_service_router.get("/service/{id}/{salon_id}")
def get_service_byid(salon_id:str,id:str,payload:dict=Depends(validate_token),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()
    if not check_salon:
        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    service_with_id = db.query(Service).filter(Service.salon_id == salon_id,Service.id == id).first()

    if not service_with_id:

        raise HTTPException(status_code=400,detail=f"No service with {id}")
    
    return {"status":200,"message":"Succesfully fetched Service", "data":service_with_id}

@staff_service_router.get("/service/{name}/{salon_id}")
def get_service_byName(name:str,salon_id:str,payload:dict=Depends(validate_token),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

    if not check_salon:
        raise HTTPException(status_code=400,detail="Salon does not exist!")

    check_service = db.query(Service).filter(Service.salon_id == salon_id,Service.name == name).first()


    if not check_service:

        raise HTTPException(status_code=200,detail="Service does not exist!")
    
    return {"status":200,"message":"Service Succesfully Fetched","data":check_service}

@staff_service_router.patch("/service/{id}")
def patch_the_service(id:str,service:SerivceP,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):
    
    check_salon = db.query(Salon).filter(Salon.id == service.salon_id).first()
    if not check_salon:
        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    check_service = db.query(Service).filter(Service.salon_id == service.salon_id,Service.id == id).first()
    
    if not check_service:

        raise HTTPException(status_code=400,detail=f"Service does not exist!")
    
    update = service.model_dump(exclude_unset=True)
    
    for field,value in update.items():
       setattr(check_service,field,value)

    db.commit()
   
    db.refresh(check_service)

    return {"status":200,"message":"Service Succesfully Updated","data":check_service}


@staff_service_router.delete("/service/{id}/{salon_id}")
def delete_service(salon_id:str,id:str,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

    if not check_salon:
        raise HTTPException(status_code=400,detail="Salon does not exist!")

    check_service = db.query(Service).filter(Service.salon_id == salon_id,Service.id == id).first()

    if not check_service:

        raise HTTPException(status_code=400,detail=f"Service does not exist!")
    
    db.delete(check_service)

    db.commit()

    return {"status":200,"message":"Service deleted Successfully!"}


#Staff Api's

@staff_service_router.post('/staff')
def create_staff(staff:StaffP,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):
    
    check_salon = db.query(Salon).filter(Salon.id == staff.salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon doest not exist!")
    
    create_staff = Staff(**staff.model_dump())
    
    db.add(create_staff)

    db.commit()

    db.refresh(create_staff)

    return {"status":200,"message":"Staff added successfully","data":create_staff}

@staff_service_router.get("/staff/{salon_id}")
def get_staff(salon_id:str,skip:int=Query(0,ge=0),limit:int=Query(0,ge=0),payload:dict=Depends(validate_token),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    query = db.query(Staff).filter(Staff.salon_id == salon_id)

    if limit > 0 :

        query.offset(skip).limit(limit)
    
    all_staff =  query.all()

    if not all_staff:

        raise HTTPException(status_code=400,detail="No Staff Available!")
    
    return {"status":200,"message":"Staffs successfully fetched","data":all_staff}

@staff_service_router.get("/staff/{id}/{salon_id}")
def get_staff_byid(id:str,salon_id:str,payload:dict=Depends(validate_token),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    check_staff = db.query(Staff).filter(Salon.id == salon_id,Staff.id == id).first()

    if not check_staff:

        raise HTTPException(status_code=400,detail="Staff does not exist!")
    
    db.commit()
    db.refresh(check_staff)
    
    return {"status":200,"message":"Succesfully fetched Staff","data":check_staff}

@staff_service_router.patch("/staff/{id}")
def patch_staff(staff:StaffP,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == staff.salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    check_staff = db.query(Staff).filter(Salon.id == staff.salon_id,Staff.id == id).first()

    if not check_staff:

        raise HTTPException(status_code=400,detail="Staff does not exist!")

    update = staff.model_dump(exclude_unset=True)

    for field,value in update.items():
        setattr(check_staff,field,value)

    db.commit()
    db.refresh(check_staff)

    return {"status":200,"message":"Staff updated Successfully","data":check_staff}

@staff_service_router.delete("/staff/{id}/{salon_id}")
def delete_staff_byid(id:str,salon_id:str,payload:dict=Depends(required_roles("admin")),db:Session=Depends(get_session)):

    check_salon = db.query(Salon).filter(Salon.id == salon_id).first()

    if not check_salon:

        raise HTTPException(status_code=400,detail="Salon does not exist!")
    
    check_staff = db.query(Staff).filter(Salon.id == salon_id,Staff.id == id).first()

    if not check_staff:

        raise HTTPException(status_code=400,detail="Staff does not exist!")
    
    db.delete(check_staff)

    db.commit()

    return {"status":200,"message":"Staff deleted Successfully!"}
