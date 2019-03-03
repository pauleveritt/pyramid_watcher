import pytest


@pytest.fixture
def app():
    from pyramid_watcher.samples.echo import main
    return main({})
