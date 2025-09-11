import fastapi
import fastapi.testclient
from fastapi.testclient import TestClient
from src.api.main import app

assert hasattr(fastapi.testclient, "TestClient"), "⚠️ TestClient missing from FastAPI"

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}