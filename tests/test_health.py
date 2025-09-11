from fastapi.testclient import TestClient  # ✅ Ensure this is from FastAPI
from src.api.main import app  # This should point to your FastAPI app instance

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}