from src.repository import filter_table_repository as repository

from src.DTO.search_filter import DataDict, FdicFail

async def filter_data_dict(pool,dataDict:DataDict):
    return await repository.filter_data_dict(pool,dataDict)

async def filter_data_dict_length(pool,dataDict:DataDict):
    return await repository.filter_data_dict_length(pool,dataDict)

async def filter_fdic_fail(pool, fdicFail:FdicFail):
    return await repository.filter_fdic_fail(pool, fdicFail)

async def filter_fdic_fail_length(pool, fdicFail:FdicFail):
    return await repository.filter_fdic_fail_length(pool, fdicFail)