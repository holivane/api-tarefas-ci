import pytest
from app import app, tarefas

@pytest.fixture
def client():
    tarefas.clear()  # Clear the tarefas list before each test
    return app.test_client()

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_add_tarefa(client):
    response = client.post('/tarefas', json={"titulo": "Estudar Flask"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["titulo"] == "Estudar Flask"
    assert data["id"] == 1

def test_listar_tarefas(client):
    client.post('/tarefas', json={"titulo": "Estudar Flask"})
    response = client.get('/tarefas')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["titulo"] == "Estudar Flask"