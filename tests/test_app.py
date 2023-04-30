from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_webhook_invalid_token():
    response = client.post("/webhook/invalid_token")
    assert response.status_code == 200
    assert response.text == "Invalid token"
