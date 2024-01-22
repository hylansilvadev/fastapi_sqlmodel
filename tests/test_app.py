from fastapi.testclient import TestClient

from fastapi_sqlmodel.app import app


def test_main_route():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert (
        response.json() == 'Bem vindo ao FastAPI + SQLModel, por: Hylan Silva'
    )
