from datetime import datetime
from pydantic import BaseModel

class MA_USERBase(BaseModel):
    id :int
    usercd:str
    password:str
    user_f_name:str
    user_l_name:str
    belonged_company_id:int
    belonged_dept_id:int
    auth_id:int
    status_id:int
    created_by:str
    created_date:datetime
    updated_by :str
    updated_date:datetime
    update_counter:int

