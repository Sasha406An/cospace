import pytest
from fastapi.testclient import TestClient
from main import app
from database import SessionLocal
from models import User, Resource, Booking

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_database():
    """Автоматическая очистка таблиц перед каждым тестом"""
    db = SessionLocal()
    try:
        db.query(Booking).delete()
        db.query(Resource).delete()
        db.query(User).delete()
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()

def test_create_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"

def test_create_user_duplicate():
    # Первый запрос создает пользователя успешно
    client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    # Второй запрос с тем же email должен выдать ошибку 400
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 400