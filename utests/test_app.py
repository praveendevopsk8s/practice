import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.json['message'] == "Welcome to the Smart Flask App!"

def test_add(client):
    res = client.get('/add/2/3')
    assert res.status_code == 200
    assert res.json['result'] == 5

def test_multiply(client):
    res = client.get('/multiply/2/4')
    assert res.status_code == 200
    assert res.json['result'] == 8
