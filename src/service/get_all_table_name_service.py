from fastapi import APIRouter

from src.repository.custom_query import custom_query as custom_query_repository

router = APIRouter()

async def get_all_table_name_service(pool):
    return await custom_query_repository(pool,"show tables")