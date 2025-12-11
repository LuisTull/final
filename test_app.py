import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Prueba que la ruta '/' devuelve el saludo correcto"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola Mundo desde Python y Docker!" in response.data
