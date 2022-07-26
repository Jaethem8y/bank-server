from fastapi import APIRouter

from src.repository.single.get_single_table import get_single_table as get_single_table_repository

router = APIRouter()

async def single_table_service(pool,table_name):
    table_name = "table_"+table_name
    return await get_single_table_repository(pool,table_name)