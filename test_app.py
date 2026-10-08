import pytest
from app import app, tasks

@pytest.fixture
def client():
    tasks.clear()
    return app.test_client()

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_create_task(client):
    response = client.post('/tasks', json={"title": "Estudar Flask"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Estudar Flask"
    assert data["id"] == 1

def test_list_tasks(client):
    client.post('/tasks', json={"title": "Estudar Flask"})
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks_list = response.get_json()
    assert len(tasks_list) == 1
    assert tasks_list[0]["title"] == "Estudar Flask"