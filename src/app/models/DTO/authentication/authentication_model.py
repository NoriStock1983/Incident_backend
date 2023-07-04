
from pydantic import BaseModel

class JWTMeta(BaseModel):
    iss: str    
    audience: str
    iat: float
    exp:float


class JWTCreds(BaseModel):
    usercd: str
    token_type:str

class JWTPayload(JWTMeta,JWTCreds):
    pass

class AccessToken(BaseModel):
    access_token: str
    token_type: str

class HASHED_PW(BaseModel):
    hashed_password:str

class TOKEN_DATA(BaseModel):
    usercd:str
