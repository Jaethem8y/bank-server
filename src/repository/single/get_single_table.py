import aiomysql

from src.repository.get_all_rows import get_all_rows

async def get_single_table(pool, table_name:str):
    return await get_all_rows(pool,table_name)