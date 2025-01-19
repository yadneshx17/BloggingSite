from fastapi.testclient import TestClient
from app.main import app
from fastapi import HTTPException

client = TestClient(app)

def test_root():
    resposne = client.get("/")
    assert resposne.status_code == 200

def test_get_users():
    res = client.get("/users/16")
    assert res.status_code == 200

def test_get_users_notfound():
    res = client.get("/users/1")
    assert res.status_code == 404

def test_create_users():
    res = client.post("/users/", json={'email': 'john909@gmail.com', 'username': 'john909', 'password': 'password123'})
    assert res.status_code == 201

# def test_delete_users():
#     res = client.delete("/users/8")
#     assert res.status_code == 204

def test_delete_users_notfound():
        res = client.post("/users/5050")
        assert res.status_code == 404

def test_update_users():
    res = client.put("/users/12", json={'email': 'updatedemail@gmail.com','username': 'UpdatedUsername', 'password' : 'updatedPassword'})
    assert res.status_code == 200       