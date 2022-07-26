from fastapi import APIRouter

from src.repository.single.get_single_table import get_single_table as get_data_dict_repository

router = APIRouter()

async def get_data_dict_service(pool):
    return await get_data_dict_repository(pool,"data_dict")