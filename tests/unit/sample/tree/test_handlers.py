from pyramid_watcher.samples.tree import ChangesetHandler


def test_changesethandler(dummy_request):
    ch = ChangesetHandler(dummy_request.config)
    assert dummy_request.config == ch.config


def test_changesethandler_call(dummy_request, dummy_changeset, mocker):
    ch = ChangesetHandler(dummy_request.config)
    root = dummy_request.registry.root
    mocker.patch.object(root, 'add_resource')
    ch(dummy_changeset)
    assert 1 == root.add_resource.call_count
