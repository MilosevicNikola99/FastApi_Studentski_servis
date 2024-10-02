from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students/",
        json = {
            "id": 4, "name": "Luka", "prezime": "Lukic", "indeks": "239/2019"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"id": 4, "name": "Luka", "prezime": "Lukic", "indeks": "239/2019"}

def test_create_existing_student():
    response = client.post(
        "/students/",
        json = {
            "id": 1, "name": "Nikola", "prezime": "Milosevic", "indeks": "197/2018"
        }
    )
    assert response.status_code == 400
    assert response.json() == { "detail":"Student already exists"}

def test_get_student():
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Nikola", "prezime": "Milosevic", "indeks": "197/2018"}


def test_get_non_existing_student():
    response = client.get("/students/10")
    assert response.status_code == 404
    assert response.json() == { "detail":"Student not found"}

    assert 200 == 205


def test_update_student():
    response = client.put("/students/2", json =  {"id": 2, "name": "Marko", "prezime": "Petrovic", "indeks": "120/2019"})
    assert response.status_code == 200
    assert response.json() == [{"id": 3, "name": "Luka", "prezime": "Lukic", "indeks": "239/2019"},
                               {"id": 1, "name": "Nikola", "prezime": "Milosevic", "indeks": "197/2018"},
                               {"id": 2, "name": "Marko", "prezime": "Petrovic", "indeks": "120/2019"},
                               {"id": 4, "name": "Luka", "prezime": "Lukic", "indeks": "239/2019"}
                               ]

def test_update_non_existing_student():
    response = client.get("/students/10")
    assert response.status_code == 404
    assert response.json() == { "detail":"Student not found"}

def test_delete_student():
    response = client.delete("/students/4")
    assert response.status_code == 200
    assert response.json() == [{"id": 3, "name": "Luka", "prezime": "Lukic", "indeks": "239/2019"},
                               {"id": 1, "name": "Nikola", "prezime": "Milosevic", "indeks": "197/2018"},
                               {"id": 2, "name": "Marko", "prezime": "Petrovic", "indeks": "120/2019"}
                               ]

def test_delete_non_existing_student():
    response = client.delete("/students/10")
    assert response.status_code == 404
    assert response.json() == { "detail":"Student not found"}