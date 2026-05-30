from fastapi.testclient import TestClient # it behaves like app=FastAPI()
from app.main import app

client = TestClient(app)
# do test via - pytest tests/

def test_eligibility_pass(): # without running the server, we can test the endpoint directly using TestClient
    payload = {
        'income': 60000,
        'age': 25,
        'employment_status': 'employed'
    }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligible': True}


def test_eligibility_fail():
    payload = {
        'income': 30000,
        'age': 18,
        'employment_status': 'unemployed'
    }
    response = client.post('/loan-eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligible': False}