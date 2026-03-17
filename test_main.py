import os

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Secure API is running"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_health_live():
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}

@pytest.mark.integration
def test_dependency_health():
    if not (os.environ.get("POSTGRES_HOST") and os.environ.get("REDIS_HOST")):
        pytest.skip("Dependency hosts not configured")
    response = client.get("/health/deps")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["dependencies"]["postgres"]["status"] == "ok"
    assert body["dependencies"]["redis"]["status"] == "ok"
