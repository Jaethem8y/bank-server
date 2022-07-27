from sys import prefix
from fastapi import APIRouter

from src.controller import single_table_controller as controller

SINGLE = "/single"

router = APIRouter()

router.include_router(controller.get_all_table_name,prefix="tables")
router.include_router(controller.describe_single_table_controller, prefix=SINGLE)
router.include_router(controller.get_single_table, prefix=SINGLE)


