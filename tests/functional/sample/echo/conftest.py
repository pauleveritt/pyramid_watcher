from pytest import fixture
from pytest_toolbox import mktree
from webtest import TestApp


tree = {
    'foo': {
        'bar.txt': 'bar',
        'spam.py': 'whatever',
        'spam.pyc': 'splosh',
        'recursive_dir': {
            'a.js': 'boom',
        },
        '.git': {
            'x': 'y',
        }
    }
}


@fixture
def app(tmpdir) -> TestApp:
    mktree(tmpdir, tree)
    from pyramid_watcher.samples.echo import main

    app = main({}, content_root=str(tmpdir))
    yield app
