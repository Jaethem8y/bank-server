from sys import prefix
from fastapi import APIRouter

from src.controller import util_controller
from src.controller import single_table_controller 

router = APIRouter()

router.include_router(util_controller.router)
router.include_router(single_table_controller.router,prefix="/single")



