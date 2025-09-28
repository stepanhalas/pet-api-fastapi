import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert r.json()["message"] == "Welcome to Pet API!"

def test_get_pets():
    r = requests.get(f"{BASE_URL}/pets")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_pet():
    new_pet = {"name": "Fibi", "type": "dog"}
    r = requests.post(f"{BASE_URL}/pets", json=new_pet)
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Fibi"
    assert data["type"] == "dog"
    assert "id" in data
