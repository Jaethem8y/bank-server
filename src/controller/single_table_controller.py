from fastapi import APIRouter, Request

from src.service import single_tables_service as service

router = APIRouter()

@router.get("/tables")
async def get_all_table_name(request:Request):
    return await service.get_all_table_names(request.state.pool)

@router.get("/{table_name}")
async def get_single_table(request:Request,table_name:str):
    return await service.get_single_table(request.state.pool, table_name)

    
@router.get("/describe/{table_name}")
async def describe_single_table_controller(request:Request,table_name:str):
    print("here")
    return await service.describe_single_table_service(request.state.pool, table_name)