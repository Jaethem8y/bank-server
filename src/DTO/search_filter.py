from typing import List, Union
from pydantic import BaseModel

class DataDict(BaseModel):
    item_code: Union[str, None] = None
    meaning: Union[str, None] = None
    start: int = 0

class FdicFail(BaseModel):
    FDICCertificateNumber: Union[int, None] = None
    BankName: Union[str, None] = None 
    City: Union[str, None] = None
    ST: Union[str, None] = None
    AcquiringInstitution: Union[str, None] = None
    ClosingDate: Union[List[str], None] = None
    start: int = 0
