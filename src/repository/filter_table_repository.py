from src.repository import sql_methods as sql

from src.DTO.search_filter import DataDict

async def filter_data_dict(pool, dataDict:DataDict):
    query = "SELECT * FROM data_dict Where 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += "Limit " +str(dataDict.start) + "," + str(dataDict.start+10000) +";"
    return await sql.get_multiple_rows(pool,query)

async def filter_data_dict_length(pool, dataDict:DataDict):
    query = "SELECT COUNT(*) AS length FROM data_dict Where 1 = 1 "
    if dataDict.item_code != None:
        query += "AND item_code LIKE \'%" + dataDict.item_code + "%\' "
    if dataDict.meaning != None:
        query += "AND meaning LIKE \'%" + dataDict.meaning + "%\' "
    query += ";"
    return await sql.get_single_row(pool,query)