from app.api.routes import MaCodeController
from fastapi import APIRouter

apirouter = APIRouter()

apirouter.include_router(MaCodeController.router, prefix="/macode",tags=["macode"])
