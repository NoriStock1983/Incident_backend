from ctypes import cast
from typing import List
from pydantic import AnyHttpUrl, BaseSettings
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# WebAPIの情報
APP_TITLE = "IncidentManagement"
APP_VERSION = "0.0.1"
API_PRESFIX = "/api"

# DB接続情報
DB_NAME = "postgresql"
POSTGRES_SERVER = config("POSTGRES_SERVER",cast=str)
POSTGRES_USER = config("POSTGRES_USER",cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD",cast=Secret)
POSTGRES_PORT = config("POSTGRES_PORT",cast=str,default="5432")
POSTGRES_DB = config("POSTGRES_DB",cast=str)
# DB接続文字列作成
DB_ACCESS_URL = f"{DB_NAME}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# JWT
ACCESS_TOKEN_EXPIRE_MINIUTES = 10               # 10miniutes
REFRESH_TOKEN_EXPIRE_MINIUTES = 60 * 24 * 7     # 7days
JWT_ALGORITHM = "HS256"
JWT_SECRET_KEY = config("JWT_SECRET_KEY",cast=str)
JWT_REFRESH_SECRET_KEY = config("JWT_REFRESH_SECRET_KEY",cast=str)
JWT_AUDIENCE = "a0006802"
JWT_ISS = "IncidentManagement.com"
ACCESS_TOKEN = "ACCESS_TOKEN"
REFRESH_TOKEN="REFRESH_TOKEN"

# システム内での利用