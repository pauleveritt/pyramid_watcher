from pyramid_watcher.samples.tree import main
from pytest import fixture
from pytest_toolbox import mktree
from webtest import TestApp

tree = {
    'about.md': 'title: Some Dummy Doc\n---\nWe are *here*.',
}


@fixture
def app(tmpdir) -> TestApp:
    mktree(tmpdir, tree)
    app = main({}, content_root=str(tmpdir))
    yield app
