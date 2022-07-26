from fastapi import APIRouter, Request

from src.repository.custom_query import custom_query

router = APIRouter()

async def describe_single_table_service(pool,table_name):
    if table_name != "data_dict" and table_name != "fdic_faile":
        table_name = "table_" + table_name
    query = "describe " + table_name + ";"
    return await custom_query(pool,query)