
from app.models.DAO.MaCodeRepository import MaCodeRepository
from fastapi import APIRouter
import logging

router = APIRouter()

# MA_CODEに登録されているデータを全件取得する。
@router.get("/all")
async def get_all_macodde():
    all_ma_code = MaCodeRepository.select_all_macode()
    
    return all_ma_code

@router.get("/getbymacodeid/{codeid}")
async def get_by_macode_id(codeid: int):
    getbyid_macode = MaCodeRepository.select_by_macode_id(codeid)
    return getbyid_macode

@router.get("/getbymacodecd/{codecd}")
async def get_by_macode_id(codecd: str):
    getbycodecd_macode = MaCodeRepository.select_by_macode_cd(codecd)
    return getbycodecd_macode
