from fastapi import APIRouter

from src.repository.single.get_single_table import get_single_table as get_fdic_fail_repository

router = APIRouter()

async def get_fdic_fail_service(pool):
    return await get_fdic_fail_repository(pool,"fdic_fail")