import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'active' in rv.data

def test_prediction(client):
    payload = {
        "sleep_hours": 7,
        "study_hours": 6,
        "physical_activity": 30,
        "social_interaction": 60,
        "screen_time": 4,
        "diet_quality": 8,
        "heart_rate": 72,
        "anxiety_score": 45,
        "journal_entry": "I am feeling a bit tired but okay."
    }
    rv = client.post('/api/predict', json=payload)
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['success'] == True
    assert 'prediction' in json_data['data']
