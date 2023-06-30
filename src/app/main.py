from fastapi import FastAPI
from app.api.router import apirouter

app = FastAPI(title="Incident",version="0.0.1")

app.include_router(apirouter, prefix="/api")