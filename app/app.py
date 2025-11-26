from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from .config.db_connection import Base,engine
from .routes.staff_service_routes import staff_service_router
from .routes.user_route import user_router
from .routes.booking_route import booking_router

from .models.user_model import User
from .models.staff_service_model import Salon,Service,Staff

app=FastAPI(title="Salon Management")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)


@app.get("/")
def root():
    return {"message","This is a Salon Management Project"}


app.include_router(staff_service_router)
app.include_router(user_router)
app.include_router(booking_router)