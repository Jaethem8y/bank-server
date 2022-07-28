from fastapi import APIRouter, Request

from src.service import filter_table_service as service

from src.DTO.search_filter.DataDict import DataDict

router = APIRouter()

@router.post("/single/data_dict")
async def filter_data_dict(request:Request, dataDict:DataDict):
    return await service.filter_data_dict(request.state.pool,dataDict)

@router.post("/length/data_dict")
async def filter_data_dict(request:Request, dataDict:DataDict):
    return await service.filter_data_dict_length(request.state.pool,dataDict)