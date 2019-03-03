from pytest import fixture

from pytest_toolbox import mktree


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
def app(tmpdir):
    mktree(tmpdir, tree)
    from pyramid_watcher.samples.echo import main

    app = main({}, content_root=str(tmpdir))
    app.registry['watcher'].stop()
    yield app
