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
    response = client.post('/tasks', json={"title": "Study Flask"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Study Flask"
    assert data["id"] == 1


def test_list_tasks(client):
    client.post('/tasks', json={"title": "Study Flask"})
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks_list = response.get_json()
    assert len(tasks_list) == 1
    assert tasks_list[0]["title"] == "Study Flask"


def test_create_task_without_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400


def test_create_task_with_null_body(client):
    response = client.post(
        '/tasks',
        data='null',
        content_type='application/json'
    )
    assert response.status_code == 400
