from src.repository import table_length_repository as repository

async def get_data_dict_length(pool, item_code:str, meaning:str):
    return await repository.get_data_dict_length(pool, item_code, meaning)

async def get_fdic_fail_length(pool, FDICCertificateNumber:str, BankName:str, City:str, ST:str, AcquiringInstitution:str, startClosingDate:str,endClosingDate:str):
    return await repository.get_fdic_fail_length(pool,FDICCertificateNumber, BankName, City, ST, AcquiringInstitution, startClosingDate, endClosingDate)

# query single table length (# of rows)
async def get_single_table_length(pool, table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table_length(pool,table_name)