from src.repository import sql_methods as sql

async def get_data_dict(pool, item_code:str, meaning:str,start:int):
    query = "SELECT * FROM data_dict " 
    query += "WHERE item_code LIKE \'%" + item_code + "%\' "
    query += "AND meaning LIKE \'%" + meaning +"%\' "
    query += "LIMIT " + str(start) + "," + str(start +10000) + ";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def get_fdic_fail(pool, FDICCertificateNumber:str, BankName:str, City:str, ST:str, AcquiringInstitution:str, startClosingDate:str,endClosingDate:str,start:int):
    query = "SELECT * FROM fdic_fail "
    query += "WHERE FDICCertificateNumber = \'%" + FDICCertificateNumber + "%\' "
    # query += "AND BankName LIKE  \'%" + BankName + "%'\' "
    # query += "AND City LIKE \'%" + City + "%\' "
    # query += "AND ST LIKE \'%" + ST + "%\' "
    # query += "AND AcquiringInstitution \'%" + AcquiringInstitution + "%\' "
    # query += "AND ClosingDate <= \'" + startClosingDate + "\' "
    # query += "AND ClosingDate >= \'" + endClosingDate + "\' "
    query += "LIMIT " + str(start) + "," + str(start+10000) + ";"  
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def get_single_table(pool,table_name:str):
    query = "SELECT * FROM " + table_name +";"
    return await sql.get_multiple_rows(pool, query)

