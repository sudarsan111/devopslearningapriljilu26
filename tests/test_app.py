import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_exists():
    """Test that the Flask app is importable."""
    assert app is not None

def test_app_is_testing(client):
    """Test that app is in testing mode."""
    assert app.config['TESTING'] is True
