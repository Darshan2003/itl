from fastapi import  APIRouter, Depends
from src.models.cars_model import Cars
from src.database.cars_db import get_all_cars, add_cars, update_cars, delete_cars, cars_model, login_admin, create_admin
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="",
    tags=["Application"],
    responses={404: {"description": "Not found"}},
)

class Admin(BaseModel):
    admin_id: str
    password: str

@router.get("/cars")
def get_all(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    admin_id = Authorize.get_jwt_subject()
    return get_all_cars(admin_id)

@router.get("/cars/{id}")
def get_cars(id, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    admin_id = Authorize.get_jwt_subject()
    return cars_model(id, admin_id)

@router.post("/cars")
def create_cars(cars: Cars, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    admin_id = Authorize.get_jwt_subject()
    add_cars(cars.id, cars.name, cars.price, cars.company, admin_id)
    return {"SUCCESS": "cars added successfully"}

@router.put("/cars")
def cars_update(cars: Cars, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    admin_id = Authorize.get_jwt_subject()
    update_cars(cars.id, cars.name, cars.price, cars.company, admin_id)
    return {"SUCCESS": "cars updated successfully"}

@router.delete("/cars")
def cars_delete(id, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    admin_id = Authorize.get_jwt_subject()
    delete_cars(id, admin_id)
    return {"SUCCESS": "cars deleted successfully"}

@router.post('/login')
def login(admin: Admin, Authorize: AuthJWT = Depends()):
    if login_admin(admin.admin_id, admin.password):
        return {"ERROR": "Invalid Admin"}

    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=admin.admin_id)
    return {"JWT": access_token}

@router.post('/signup')
def signup(admin: Admin, Authorize: AuthJWT = Depends()):
    create_admin(admin.admin_id, admin.password)
    access_token = Authorize.create_access_token(subject=admin.admin_id)
    return {"JWT": access_token}
