from pytest import fixture
from pytest_toolbox import mktree
from webtest import TestApp


tree = {
    'foo': {
        'about.md': 'title: Some Dummy Doc\n---\nWe are *here*.',
    }
}


@fixture
def app(tmpdir) -> TestApp:
    mktree(tmpdir, tree)
    from pyramid_watcher.samples.tree import main

    app = main({}, content_root=str(tmpdir))
    yield app
