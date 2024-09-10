from fastapi.testclient import TestClient

from routers.subject import app

client = TestClient(app)


def test_create_subject():
    response = client.post(
        "/subjects/",
        json = {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 200
    assert response.json() ==  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_create_existing_subject():
    response = client.post(
        "/subjects/",
        json =  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 400
    assert response.json() == { "detail":"Subject already exists"}

def test_get_subject():
    response = client.get("/subjects/M102")
    assert response.status_code == 200
    assert response.json() == {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_get_non_existing_subject():
    response = client.get("/subjects/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Subject not found"}

def test_update_student():
    response = client.put("/subjects/M102",
                          json =  {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}
                          )
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "M101", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M10", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6},
                               {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}]


def test_update_non_existing_student():
    response = client.get("/subjects/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Subject not found"}

def test_delete_student():
    response = client.delete("/subjects/M102")
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "M101", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M10", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6}]


def test_delete_non_existing_student():
    response = client.delete("/subjects/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Subject not found"}