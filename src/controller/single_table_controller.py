from fastapi import APIRouter, Request

from src.service import single_tables_service as service


router = APIRouter()

@router.get("/data_dict")
async def get_data_dict(request:Request,start:int=0):
    return await service.get_data_dict(request.state.pool, start)

@router.get(path="/fdic_fail")
async def get_fdic_fail(request:Request,FDICCertificateNumber:str="", BankName:str="", City:str="", ST:str="", AcquiringInstitution:str="", startClosingDate:str="1950-01-01",endClosingDate:str="2050-01-01",start:int=0):
    return await service.get_fdic_fail(request.state.pool,FDICCertificateNumber, BankName, City, ST, AcquiringInstitution, startClosingDate, endClosingDate,start)

@router.get(path="/FDICCertificateNumber")
async def get_FDICCertificateNumber(request:Request):
    return await service.get_single_table(request.state.pool,"FDICCertificateNumber")

@router.get(path="/FinancialInstitutionFilingType")
async def get_FDICCertificateNumber(request:Request):
    return await service.get_single_table(request.state.pool,"FinancialInstitutionFilingType")

@router.get(path="/FinancialInstitutionZipCode")
async def get_FinancialInstitutionZipCode(request:Request):
    return await service.get_single_table(request.state.pool,"FinancialInstitutionZipCode")

@router.get(path="/OCCCharterNumber")
async def get_OCCCharterNumber(request:Request):
    return await service.get_single_table(request.state.pool,"OCCCharterNumber")

@router.get(path="/OTSDocketNumber")
async def get_OTSDocketNumber(request:Request):
    return await service.get_single_table(request.state.pool,"OTSDocketNumber")

@router.get(path="/PrimaryABARoutingNumber")
async def get_PrimaryABARoutingNumber(request:Request):
    return await service.get_single_table(request.state.pool,"PrimaryABARoutingNumber")


@router.get("/{table_name}")
async def get_single_table(request:Request,table_name:str,start:int=None, end:int=None, bank_id:str=None, start_year:int=None, end_year:int=None, start_quarter:int=None, end_quarter:int=None,start_score:int=None, end_score:int=None):
    return await service.get_single_table(request.state.pool, table_name)
