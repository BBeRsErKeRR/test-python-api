import pytest
from app import create_app

@pytest.yield_fixture(scope='session')
def _app():
    _app = create_app(None, None)
    app_context = _app.app_context()
    app_context.push()

    yield _app

    app_context.pop()

@pytest.fixture()
def client(_app):
    return _app.test_client()
