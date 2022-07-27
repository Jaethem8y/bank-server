from src.repository import single_table_repository as repository

# query table by table_name
async def get_single_table(pool, table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table(pool,table_name)

# query describe table_name
async def describe_single_table_service(pool,table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.describe_single_table(pool,table_name)

# query showing all tables
async def get_all_table_names(pool):
    return await repository.get_all_table_name(pool)

# query single table length (# of rows)
async def get_single_table_length(pool, table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table_length(pool,table_name)