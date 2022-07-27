from fastapi import APIRouter, Request

from src.service import table_length_service as service

router = APIRouter()

@router.get(path="/data_dict")
async def get_data_dict_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"data_dict")

@router.get(path="/fdic_fail")
async def get_data_dict_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"fdic_fail")

@router.get(path="/FDICCertificateNumber")
async def get_FDICCertificateNumber_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"FDICCertificateNumber")

@router.get(path="/FinancialInstitutionFilingType")
async def get_FDICCertificateNumber_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"FinancialInstitutionFilingType")

@router.get(path="/FinancialInstitutionZipCode")
async def get_FinancialInstitutionZipCode_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"FinancialInstitutionZipCode")

@router.get(path="/OCCCharterNumber")
async def get_OCCCharterNumber_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"OCCCharterNumber")

@router.get(path="/OTSDocketNumber")
async def get_OTSDocketNumber_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"OTSDocketNumber")

@router.get(path="/PrimaryABARoutingNumber")
async def get_PrimaryABARoutingNumber_length(request:Request):
    return await service.get_single_table_length(request.state.pool,"PrimaryABARoutingNumber")

@router.get(path="/{table_name}")
async def get_table_length(request:Request,table_name:str):
  return await service.get_single_table_length(request.state.pool,table_name)