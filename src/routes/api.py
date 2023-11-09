from fastapi import APIRouter
from src.controllers import cars_endp

router = APIRouter()
router.include_router(cars_endp.router)
