from src.repository import sql_methods as sql

from src.DTO.search_filter import DataDict, FdicFail

async def filter_data_dict(pool, dataDict:DataDict):
    query = "SELECT * FROM data_dict WHERE 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += "Limit " +str(dataDict.start) + "," + str(dataDict.start+10000) +";"
    return await sql.get_multiple_rows(pool,query)

async def filter_data_dict_length(pool, dataDict:DataDict):
    query = "SELECT COUNT(*) AS length FROM data_dict WHERE 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += ";"
    return await sql.get_single_row(pool,query)

async def filter_fdic_fail(pool, fdicFail:FdicFail):
    query = "SELECT * FROM fdic_fail WHERE 1 = 1 "
    if fdicFail.FDICCertificateNumber != None:
        query += "AND FDICCertificateNumber = " + str(fdicFail.FDICCertificateNumber) + " "
    if fdicFail.BankName != None:
        query += "AND BankName LIKE \'%" + fdicFail.BankName + "%\' " 
    if fdicFail.City != None:
        query += "AND City LIKE \'%" + fdicFail.City + "%\' "
    if fdicFail.ST != None:
        query += "AND ST LIKE \'%" + fdicFail.ST + "%\'" 
    if fdicFail.AcquiringInstitution != None:
        query += "AND AcquiringInstitution LIKE \'%" + fdicFail.AcquiringInstitution + "%\' "
    if fdicFail.ClosingDate != None:
        query += "AND ClosingDate BETWEEN " "\'"+ fdicFail.ClosingDate[0] +"\'" + "AND " + "\'" + fdicFail.ClosingDate[1] + "\' "
    query += "Limit " +str(fdicFail.start) + "," + str(fdicFail.start+10000) +";"
    print(query)
    return await sql.get_multiple_rows(pool,query)

async def filter_fdic_fail_length(pool, fdicFail:FdicFail):
    query = "SELECT COUNT(*) AS length FROM fdic_fail WHERE 1 = 1 "
    if fdicFail.FDICCertificateNumber != None:
        query += "AND FDICCertificateNumber = " + str(fdicFail.FDICCertificateNumber) + " "
    if fdicFail.BankName != None:
        query += "AND BankName LIKE \'%" + fdicFail.BankName + "%\' " 
    if fdicFail.City != None:
        query += "AND City LIKE \'%" + fdicFail.City + "%\' "
    if fdicFail.ST != None:
        query += "AND ST LIKE \'%" + fdicFail.ST + "%\'" 
    if fdicFail.AcquiringInstitution != None:
        query += "AND AcquiringInstitution LIKE \'%" + fdicFail.AcquiringInstitution + "%\' "
    if fdicFail.ClosingDate != None:
        query += "AND ClosingDate BETWEEN " "\'"+ fdicFail.ClosingDate[0] +"\'" + "AND " + "\'" + fdicFail.ClosingDate[1] + "\' "
    query += ";"
    print(query)
    return await sql.get_multiple_rows(pool,query)
