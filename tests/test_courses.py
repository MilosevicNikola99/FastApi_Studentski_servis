from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_create_course():
    response = client.post(
        "/courses/",
        json = {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 200
    assert response.json() ==  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_create_existing_course():
    response = client.post(
        "/courses/",
        json =  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 400
    assert response.json() == { "detail":"Course already exists"}

def test_get_course():
    response = client.get("/courses/M102")
    assert response.status_code == 200
    assert response.json() == {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_get_non_existing_course():
    response = client.get("/courses/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Course not found"}

def test_update_course():
    response = client.put("/courses/M102",
                          json =  {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}
                          )
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "P120", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M101", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6},
                               {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}]


def test_update_non_existing_student():
    response = client.get("/courses/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Course not found"}

def test_delete_course():
    response = client.delete("/courses/M102")
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "P120", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M101", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6}]


def test_delete_non_existing_course():
    response = client.delete("/courses/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Course not found"}