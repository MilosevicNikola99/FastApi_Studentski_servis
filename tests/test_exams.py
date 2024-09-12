from fastapi.testclient import TestClient
import json
from ..main import app

client = TestClient(app)



def test_create_exam():
    response = client.post(
        "/exams/P140/183-2019",
        json = {
                  "datum": "10.02.2023",
                  "ocena": 7,
                  "polozen": True
                }
    )

    assert response.status_code == 200
    assert response.json() == {"sifra_predmeta": "P140", "indeks": "183-2019", "datum": "10.02.2023", "ocena": 7, "polozen": True}

def test_create_existing_exam():
    response = client.post(
        "/exams/P140/183-2019/",
        json={"sifra_predmeta": "P140", "indeks": "183-2019", "datum": "10.02.2023", "ocena": 7, "polozen": True}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Exam already exists"}

def test_get_exams():
    response = client.get("/exams")
    assert response.status_code == 200
    assert response.json() == [{"indeks": "197-2018", "sifra_predmeta": "P120", "datum": "11.05.2024", "ocena": 8, "polozen": True},
                              {"indeks": "163-2018", "sifra_predmeta": "P120", "datum": "11.05.2024", "ocena": 5, "polozen": False},
                              {"indeks": "197-2018", "sifra_predmeta": "M101", "datum": "11.05.2024", "ocena": 9, "polozen": True},
                              {"indeks": "102-2018", "sifra_predmeta": "P120", "datum": "11.02.2024", "ocena": 7, "polozen": True},
                              {"indeks": "10-2020", "sifra_predmeta": "P130", "datum": "23.09.2024", "ocena": 5, "polozen": False},
                              {"sifra_predmeta": "P140", "indeks": "183-2019", "datum": "10.02.2023", "ocena": 7, "polozen": True}]

def test_get_exams_by_sifra():
    response = client.get("/exams?sifra_predmeta=P120")
    assert response.status_code == 200
    assert response.json() == [{
        "indeks": "197-2018",
        "sifra_predmeta": "P120",
        "datum": "11.05.2024",
        "ocena": 8,
        "polozen": True
        }, {
        "indeks": "163-2018",
        "sifra_predmeta": "P120",
        "datum": "11.05.2024",
        "ocena": 5,
        "polozen": False}, {
        "indeks": "102-2018",
        "sifra_predmeta": "P120",
        "datum": "11.02.2024",
        "ocena": 7,
        "polozen": True}
    ]

def test_get_exams_by_sifra_not_found():
    response = client.get("/exams?sifra_predmeta=P1200")
    assert response.status_code == 404
    assert response.json() == {"detail":"Exams not found"}

def test_get_exams_by_indeks():
    response = client.get("/exams?indeks=197-2018")
    assert response.status_code == 200
    assert response.json() == [
  {
    "indeks": "197-2018",
    "sifra_predmeta": "P120",
    "datum": "11.05.2024",
    "ocena": 8,
    "polozen": True
  },
  {
    "indeks": "197-2018",
    "sifra_predmeta": "M101",
    "datum": "11.05.2024",
    "ocena": 9,
    "polozen": True
  }
  ]

def test_get_exams_by_indeks_not_found():
    response = client.get("/exams?indeks=1997-2018")
    assert response.status_code == 404
    assert response.json() == {"detail":"Exams not found"}

def test_get_exams_by_sifra_and_indeks():
    response = client.get("/exams?sifra_predmeta=P120&indeks=197-2018")
    assert response.status_code == 200
    assert response.json() == [{
    "indeks": "197-2018",
    "sifra_predmeta": "P120",
    "datum": "11.05.2024",
    "ocena": 8,
    "polozen": 1
  }]

def test_get_exams_by_sifra_and_indeks_not_found():
    response = client.get("/exams?sifra_predmeta=P1200")
    assert response.status_code == 404
    assert response.json() == {"detail":"Exams not found"}

def test_update_exam():
    response = client.put("/exams/P140/183-2019/10.02.2023",
                          json = {"datum": "10.02.2023",
                                "ocena": 5,
                                "polozen": False})

    assert response.status_code == 200
    assert response.json() == {'indeks': '183-2019', 'sifra_predmeta': 'P140', 'datum': '10.02.2023', 'ocena': 5, 'polozen': False}

def test_update_non_existing_exam():
    response = client.put("/exams/P1400/1833-2019/10.02.2023",
                          json={"datum": "10.02.2023",
                                "ocena": 5,
                                "polozen": False})

    assert response.status_code == 404
    assert response.json() ==  { "detail":"Exam not found"}

def test_delete_exam():
    response = client.delete("/exams/P140/183-2019/10.02.2023")
    assert response.status_code == 200
    assert response.json() == [{"indeks": "197-2018", "sifra_predmeta": "P120", "datum": "11.05.2024", "ocena": 8, "polozen": True},
                               {"indeks": "163-2018", "sifra_predmeta": "P120", "datum": "11.05.2024", "ocena": 5, "polozen": False},
                               {"indeks": "197-2018", "sifra_predmeta": "M101", "datum": "11.05.2024", "ocena": 9, "polozen": True},
                               {"indeks": "102-2018", "sifra_predmeta": "P120", "datum": "11.02.2024", "ocena": 7, "polozen": True},
                               {"indeks": "10-2020", "sifra_predmeta": "P130", "datum": "23.09.2024", "ocena": 5, "polozen": False}]


def test_delete_non_existing_exam():
    response = client.delete("/exams/P1400/183-20019/10.02.2023")
    assert response.status_code == 404
    assert response.json() == { "detail":"Exam not found"}

