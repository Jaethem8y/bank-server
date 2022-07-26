from fastapi import APIRouter

from src.controller.get_all_table_name_controller import router as get_all_table_name_router
from src.controller.single.data_dict_controller import router as data_dict_router
from src.controller.single.fdic_fail_controller import router as fdic_fail_router
from src.controller.single.single_table_controller import router as single_table_router
from src.controller.single.describe_single_table_controller import router as describe_single_table_router

SINGLE = "/single"

router = APIRouter()



router.include_router(get_all_table_name_router)
router.include_router(data_dict_router, prefix=SINGLE)
router.include_router(fdic_fail_router, prefix=SINGLE)
router.include_router(describe_single_table_router, prefix=SINGLE)
router.include_router(single_table_router, prefix=SINGLE)

