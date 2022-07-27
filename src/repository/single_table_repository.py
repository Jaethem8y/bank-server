from src.repository import sql_methods as sql

async def get_single_table(pool,table_name:str):
    query = "SELECT * FROM " + table_name +";"
    return await sql.get_multiple_rows(pool, query)

