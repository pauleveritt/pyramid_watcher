from pyramid_watcher.samples.echo.views import root


def test_homepage(dummy_context, dummy_request):
    dummy_context.changesets = [1, 2, 3]
    result = root(dummy_context, dummy_request)
    assert 'Echo Sample' == result['project']
    assert 'Dummy Title' == result['title']
    assert dummy_context.changesets == result['changesets']
