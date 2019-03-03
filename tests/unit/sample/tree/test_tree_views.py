from pyramid_watcher.samples.tree.views import root


def test_root(dummy_context, dummy_request):
    dummy_context.changesets = [1, 2, 3]
    result = root(dummy_context, dummy_request)
    assert 'Tree Sample' == result['project']
    assert 'Dummy Title' == result['context'].title
