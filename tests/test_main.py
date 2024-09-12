from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_calculate_espb():
    response = client.get("/espb/197-2018")
    assert response.status_code == 200
    assert response.json() == {"Ukupno espb": 14 }

def test_calculate_passed_exams():
    response = client.get("/statistics/197-2018")
    assert response.status_code == 200
    assert response.json() == {
                                "polozio": 2,
                                "nije polozio": 0,
                                "ukupno espb": 2
                              }