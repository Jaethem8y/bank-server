from fastapi import APIRouter, Request

from src.service.single.data_dict_service import get_data_dict_service

router = APIRouter()

@router.get("/data_dict")
async def get_data_dict(request:Request):
    return await get_data_dict_service(request.state.pool)