from app.models.DAO.MaUserRepository import MaUserRepository
from fastapi import APIRouter
import logging


router = APIRouter()

# MA_USERに登録されているデータを全件取得する。
@router.get("/all")
async def get_all_macodde():
    all_ma_user = MaUserRepository.select_all_mauser()
    
    return all_ma_user

# MA_USERに登録されているデータを全件取得する。
@router.get("/getbyusercd/{codecd}")
async def get_by_usercd(usercd: str):
    getbyusercd = MaUserRepository.select_by_mauser_cd(usercd)
    
    return getbyusercd
