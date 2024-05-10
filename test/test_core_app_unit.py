import pytest
from gutn_pi_integration.core.app import App

@pytest.fixture
def app():
    return App()

def test_app_initialization(app):
    assert isinstance(app, App)

def test_app_method(app):
    result = app.some_method()
    assert result == 'expected result'
