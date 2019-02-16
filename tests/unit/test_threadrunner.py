from pathlib import Path

from pyramid_watcher.threadrunner import ThreadRunner


def test_construction():
    def fake_callback(changes):
        return changes

    fake_path = Path('/tmp')
    tr = ThreadRunner(fake_callback, watched_path=fake_path)
    assert fake_callback == tr.callback
    assert fake_path == tr.watched_path
