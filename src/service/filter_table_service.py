from src.repository import filter_table_repository as repository

from src.DTO.search_filter import DataDict

async def filter_data_dict(pool,dataDict:DataDict):
    return await repository.filter_data_dict(pool,dataDict)

async def filter_data_dict_length(pool,dataDict:DataDict):
    return await repository.filter_data_dict_length(pool,dataDict)