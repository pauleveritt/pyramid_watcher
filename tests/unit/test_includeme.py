from pyramid_watcher import includeme


def test_includeme():
    assert 'works' == includeme(None)
