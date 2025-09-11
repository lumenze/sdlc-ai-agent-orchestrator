# src/api/main.py

from fastapi import FastAPI
from src.api.routes import health
from src.api.routes import generate_tickets

app = FastAPI()

app.include_router(health.router, prefix="/health")

app.include_router(generate_tickets.router)