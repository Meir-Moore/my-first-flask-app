import pytest
from flask import Flask
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
