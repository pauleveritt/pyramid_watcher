from pyramid_watcher.subscribers import start_threadrunner


class FakeEvent:
    pass


def test_application_created():
    event = FakeEvent()
    result = start_threadrunner(event)
    assert None is result
