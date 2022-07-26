from fastapi import APIRouter, Request

from src.service.single.single_table_service import single_table_service

router = APIRouter()

@router.get("/{table_name}")
async def get_single_table(request:Request,table_name:str):
    return await single_table_service(request.state.pool,table_name)