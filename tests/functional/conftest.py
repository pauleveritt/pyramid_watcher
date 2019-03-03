import pytest


@pytest.fixture
def testapp(app):
    from webtest import TestApp
    return TestApp(app)

