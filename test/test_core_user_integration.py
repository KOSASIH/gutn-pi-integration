import pytest
from gutn_pi_integration.core.user import User
from gutn_pi_integration.core.app import App

@pytest.fixture
def app():
    return App()

@pytest.fixture
def user():
    return User()

def test_user_initialization(user):
    assert isinstance(user, User)

def test_user_method(app, user):
    result = user.some_method(app)
    assert result == 'expected result'
