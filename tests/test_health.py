from fastapi.testclient import TestClient
from src.api.main import app  # This should already include the router

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}