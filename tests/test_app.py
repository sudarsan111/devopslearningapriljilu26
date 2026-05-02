import pytest
from app import app
import config

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_exists():
    assert app is not None

def test_app_is_testing(client):
    assert app.config['TESTING'] is True

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_config_flag_default():
    assert config.flag("nonexistent") is False

def test_config_flag_known():
    assert isinstance(config.flag("new_checkout_flow"), bool)
