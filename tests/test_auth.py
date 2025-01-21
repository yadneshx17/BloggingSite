from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_loginUser():
    res = client.post("/login", data={'username':'yadnesh@gmail.com', 'password':'password123'})

    assert res.status_code == 200

def test_registerUser():
    res = client.post("/register/", json={
    "email": "tommyVercetti@gmail.com",
    "username": "tommyVercetti",
    "password": "password123"
})
    assert res.status_code == 201