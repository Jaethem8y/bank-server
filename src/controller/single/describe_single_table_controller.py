from fastapi import APIRouter, Request

from src.service.single.describe_single_table_service import describe_single_table_service
router = APIRouter()

@router.get("/describe/{table_name}")
async def describe_single_table_controller(request:Request,table_name:str):
    print("here")
    return await describe_single_table_service(request.state.pool,table_name)