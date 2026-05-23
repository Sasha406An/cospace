from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_create_user_duplicate_email():
    # Повторный запрос с той же почтой должен выдать ошибку 400
    client.post("/users/", json={"name": "User 1", "email": "dup@example.com"})
    response = client.post("/users/", json={"name": "User 2", "email": "dup@example.com"})
    assert response.status_code == 400