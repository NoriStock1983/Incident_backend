from datetime import datetime
from pydantic import BaseModel

class MA_CODEBase(BaseModel):
    id:int
    code_1:str
    code_2:str
    code_nm_1:str
    code_nm_2:str
    Active_flg:bool
    createdby:str
    created_date:datetime
    updated_by:str
    updated_date:datetime
    update_counter:int

class Select_MA_CODE(MA_CODEBase):
    id:int
    code_1:str
    code_2:str
    code_nm_1:str
    code_nm_2:str