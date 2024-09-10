from fastapi.testclient import TestClient

from routers.exams import app

client = TestClient(app)


def test_create_exam():
    response = client.post(
        "/exams/",
        json = {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 200
    assert response.json() ==  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_create_existing_exam():
    response = client.post(
        "/exams/",
        json =  {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}
    )
    assert response.status_code == 400
    assert response.json() == { "detail":"Exam already exists"}

def test_get_exam():
    response = client.get("/exams/M102")
    assert response.status_code == 200
    assert response.json() == {"naziv": "Analiza2", "sifra_predmeta": "M102", "espb": 8}

def test_get_non_existing_exam():
    response = client.get("/exams/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Exam not found"}

def test_update_student():
    response = client.put("/exams/M102",
                          json =  {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}
                          )
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "M101", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M10", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6},
                               {"naziv": "Analiza3", "sifra_predmeta": "M102", "espb": 8}]


def test_update_non_existing_student():
    response = client.get("/exams/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Exam not found"}

def test_delete_student():
    response = client.delete("/exams/M102")
    assert response.status_code == 200
    assert response.json() == [{"naziv": "Analiza1", "sifra_predmeta": "M101", "espb": 8},
                               {"naziv": "Razvoj softvera", "sifra_predmeta": "P107", "espb": 6},
                               {"naziv": "Algebra", "sifra_predmeta": "M10", "espb": 6},
                               {"naziv": "Geometrija", "sifra_predmeta": "M110", "espb": 6}]


def test_delete_non_existing_student():
    response = client.delete("/exams/P2000")
    assert response.status_code == 404
    assert response.json() == { "detail":"Exam not found"}