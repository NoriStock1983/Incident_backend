from fastapi import APIRouter


router = APIRouter()

# ログイン処理
@router.post("/token")
async def auth_login():
    pass