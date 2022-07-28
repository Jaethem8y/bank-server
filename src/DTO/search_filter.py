from typing import Union
from pydantic import BaseModel

class DataDict(BaseModel):
    item_code: Union[str, None] = None
    meaning: Union[str, None] = None
    start: int = 0
