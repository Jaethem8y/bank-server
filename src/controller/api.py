from sys import prefix
from fastapi import APIRouter

from src.controller import single_table_controller as controller

SINGLE = "/single"

router = APIRouter()

router.include_router(controller.router,prefix=SINGLE)



