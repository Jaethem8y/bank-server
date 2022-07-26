from fastapi import APIRouter, Request

from src.service.single.fdic_fail_service import get_fdic_fail_service
router = APIRouter()

@router.get("/fdic_fail")
async def get_data_dict(request:Request):
    return await get_fdic_fail_service(request.state.pool)