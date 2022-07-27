from src.repository import sql_methods as sql

async def get_data_dict_length(pool, item_code:str, meaning:str):
    query = "SELECT COUNT(*) FROM data_dict " 
    query += "WHERE item_code LIKE \'%" + item_code + "%\' "
    query += "AND meaning LIKE \'%" + meaning +"%\';"
    print(query)
    return await sql.get_single_row(pool,query)

async def get_fdic_fail_length(pool, FDICCertificateNumber:str, BankName:str, City:str, ST:str, AcquiringInstitution:str, startClosingDate:str,endClosingDate:str):
    query = "SELECT COUNT(*) FROM fdic_fail "
    query += "WHERE FDICCertificateNumber Like \'%" + FDICCertificateNumber + "%\' "
    # query += "AND BankName LIKE  \'%" + BankName + "%'\' "
    # query += "AND City LIKE \'%" + City + "%\' "
    # query += "AND ST LIKE \'%" + ST + "%\' "
    # query += "AND AcquiringInstitution \'%" + AcquiringInstitution + "%\' "
    # query += "AND ClosingDate <= \'" + startClosingDate + "\' "
    # query += "AND ClosingDate >= \'" + endClosingDate + "\';"
    print("\n\n\n\n"+query+"\n\n\n\n") 
    return await sql.get_single_row(pool,query)

async def get_single_table_length(pool, table_name:str):
    query = "SELECT COUNT(*) AS length FROM " + table_name +";"
    return await sql.get_single_row(pool,query)