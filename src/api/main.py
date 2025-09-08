# src/api/main.py

from fastapi import FastAPI
from src.api.routes import health

app = FastAPI()

app.include_router(health.router, prefix="/health")