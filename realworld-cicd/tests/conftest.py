import pytest
from src.app import create_app
from src import models

@pytest.fixture(autouse=True)
def clear_store():
    models.clear()
    yield
    models.clear()

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
