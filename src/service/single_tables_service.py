from src.repository import single_table_repository as repository

async def get_data_dict(pool, start:int):
    return await repository.get_data_dict(pool,start)

async def get_fdic_fail(pool, FDICCertificateNumber:str, BankName:str, City:str, ST:str, AcquiringInstitution:str, startClosingDate:str,endClosingDate:str,start:int):
    return await repository.get_fdic_fail(pool,FDICCertificateNumber, BankName, City, ST, AcquiringInstitution, startClosingDate, endClosingDate, start)

# query table by table_name
async def get_single_table(pool, table_name:str):
    if table_name != "data_dict" and table_name != "fdic_fail":
        table_name = "table_" + table_name
    return await repository.get_single_table(pool,table_name)



