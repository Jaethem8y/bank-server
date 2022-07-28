from src.repository import sql_methods as sql

async def get_data_dict_length(pool):
    query = "SELECT COUNT(*) AS length FROM data_dict " 
    print(query)
    return await sql.get_single_row(pool,query)

async def get_fdic_fail_length(pool):
    query = "SELECT COUNT(*) AS length FROM fdic_fail "
    print(query) 
    return await sql.get_single_row(pool,query)

async def get_single_table_length(pool, table_name:str):
    query = "SELECT COUNT(*) AS length FROM " + table_name +";"
    return await sql.get_single_row(pool,query)