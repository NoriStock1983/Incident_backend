from telnetlib import STATUS
from app.models.DAO.authentication.AuthenticationRepository import AuthenticationRepositry
from app.services.authenticationService import AuthenticationService,JWTService
from fastapi import APIRouter

from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

# ログイン処理
@router.post("/token")
async def auth_login(response: Response,form_data:OAuth2PasswordRequestForm = Depends()):
    
    #入力されたユーザCDがDB上に存在しているかチェックを行う。
    user = AuthenticationRepositry.checkusercd(form_data.username)

    if user == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= 'Could not validate credentials',
            headers= {"WWW-Authenticate":"Bearer"},
        )

    # 入力されたusercdからPWを取得する。
    hash_pw = AuthenticationRepositry.get_hashpw(form_data.username)

    # 入力されたPWとDBに登録されているハッシュ化されたPWを比較する。
    checkpw = AuthenticationService.verify_password(form_data.password,hash_pw)
    # 入力されたPWとハッシュ化されたPWが同じかチェックを行う。
    if checkpw == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= 'Could not validate credentials',
            headers= {"WWW-Authenticate":"Bearer"},
        )

    # 存在すれば、Access Tokenを発行する。
    access_token = JWTService.create_access_token(form_data.username)

    # 作成したAccessTokenをcookieに設定する。
    response.set_cookie(key="access_token", value=access_token)

    return {"access_token": access_token, "token_type": "bearer"}