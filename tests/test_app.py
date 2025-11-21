import pytest
from fastapi.testclient import TestClient
from src.app.app import app

def test_health_client():
    with TestClient(app) as client:
        res = client.get('/health')
        assert res.status_code == 200

def test_prediction():
    with TestClient(app) as client:
        #add payload later for predictions
        res = client.post('/predict',json={}) #json = {} the brackets to be replaced
        assert res.status_code == 200 
        body = res.json()
        assert "prediction" in body