from fastapi import APIRouter, Request

from src.service.get_all_table_name_service import get_all_table_name_service

router = APIRouter()

@router.get("/tables")
async def get_all_table_name(request:Request):
    return await get_all_table_name_service(request.state.pool)