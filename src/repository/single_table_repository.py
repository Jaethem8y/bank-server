from src.repository import sql_methods as sql

async def get_data_dict(pool,start:int):
    query = "SELECT * FROM data_dict " 
    query += "LIMIT " + str(start) + "," + str(start +10000) + ";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def get_fdic_fail(pool, start:int):
    query = "SELECT * FROM fdic_fail "
    query += "LIMIT " + str(start) + "," + str(start+10000) + ";"  
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def get_single_table(pool,table_name:str):
    query = "SELECT * FROM " + table_name +";"
    return await sql.get_multiple_rows(pool, query)

