import pytest
from client.main import WebSocketClient


@pytest.fixture()
def url():
    return "http://localhost:8080/test"


@pytest.fixture(scope="session")
def client():
    return WebSocketClient()
