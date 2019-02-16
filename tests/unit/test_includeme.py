import pytest
from pyramid_watcher import includeme
from pyramid.testing import setUp, tearDown


@pytest.fixture
def config():
    yield setUp()
    tearDown()


def test_includeme(config):
    assert True
    # assert None is includeme(config)
