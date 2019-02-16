from time import sleep

from pyramid_watcher.watchgod_watcher import (
    AllWatcher,
    DefaultWatcher,
    FileChangeInfo,
    PythonWatcher,
    RegExpWatcher
)
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


def test_add(tmpdir):
    watcher = AllWatcher(str(tmpdir))
    changes = watcher.check()
    assert changes == set()

    sleep(0.01)
    tmpdir.join('foo.txt').write('foobar')

    changes = watcher.check()
    assert changes == {(FileChangeInfo.added, str(tmpdir.join('foo.txt')))}


def test_modify(tmpdir):
    mktree(tmpdir, tree)

    watcher = AllWatcher(str(tmpdir))
    assert watcher.check() == set()

    sleep(0.01)
    tmpdir.join('foo/bar.txt').write('foobar')

    assert watcher.check() == {(FileChangeInfo.modified, str(tmpdir.join('foo/bar.txt')))}


def test_delete(tmpdir):
    mktree(tmpdir, tree)

    watcher = AllWatcher(str(tmpdir))

    sleep(0.01)
    tmpdir.join('foo/bar.txt').remove()

    assert watcher.check() == {(FileChangeInfo.deleted, str(tmpdir.join('foo/bar.txt')))}


def test_ignore_file(tmpdir):
    mktree(tmpdir, tree)

    watcher = DefaultWatcher(str(tmpdir))

    sleep(0.01)
    tmpdir.join('foo/spam.pyc').write('foobar')

    assert watcher.check() == set()


def test_ignore_dir(tmpdir):
    mktree(tmpdir, tree)

    watcher = DefaultWatcher(str(tmpdir))

    sleep(0.01)
    tmpdir.join('foo/.git/abc').write('xxx')

    assert watcher.check() == set()


def test_python(tmpdir):
    mktree(tmpdir, tree)

    watcher = PythonWatcher(str(tmpdir))

    sleep(0.01)
    tmpdir.join('foo/spam.py').write('xxx')
    tmpdir.join('foo/bar.txt').write('xxx')

    assert watcher.check() == {(FileChangeInfo.modified, str(tmpdir.join('foo/spam.py')))}


def test_regexp(tmpdir):
    mktree(tmpdir, tree)

    re_files = r'^.*(\.txt|\.js)$'
    re_dirs = r'^(?:(?!recursive_dir).)*$'

    watcher = RegExpWatcher(str(tmpdir), re_files, re_dirs)
    changes = watcher.check()
    assert changes == set()

    sleep(0.01)
    tmpdir.join('foo/spam.py').write('xxx')
    tmpdir.join('foo/bar.txt').write('change')
    tmpdir.join('foo/borec.txt').write('ahoy')
    tmpdir.join('foo/borec-js.js').write('peace')
    tmpdir.join('foo/recursive_dir/b.js').write('borec')

    assert watcher.check() == {
        (FileChangeInfo.modified, str(tmpdir.join('foo/bar.txt'))),
        (FileChangeInfo.added, str(tmpdir.join('foo/borec.txt'))),
        (FileChangeInfo.added, str(tmpdir.join('foo/borec-js.js')))}


def test_does_not_exist(caplog):
    AllWatcher('/foo/bar')
    assert "error walking file system: FileNotFoundError [Errno 2] No such file or directory: '/foo/bar'" in caplog.text
