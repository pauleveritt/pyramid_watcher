from pytest import fixture
from webtest import TestApp


@fixture
def app() -> TestApp:
    from pyramid_watcher.samples.echo import main

    app = main({}, content_root='/tmp')
    yield app
