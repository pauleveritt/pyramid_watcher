from pathlib import Path

from pyramid_watcher.samples.tree import ChangesetHandler, Root
from pyramid_watcher.samples.tree.resources.base_resources import Resource


def test_changesethandler(dummy_request, dummy_tmpdir):
    root = dummy_request.registry.root
    ch = ChangesetHandler(dummy_request.config, root, dummy_tmpdir)
    assert dummy_request.config == ch.config


def test_changesethandler_call(dummy_request, dummy_tmpdir, dummy_changeset, mocker):
    root = dummy_request.registry.root
    ch = ChangesetHandler(dummy_request.config, root, dummy_tmpdir)
    mocker.patch.object(ch, 'add_resource')
    ch(dummy_changeset)
    assert 1 == ch.add_resource.call_count


def test_changesethandler_initialize(dummy_request, dummy_tmpdir, mocker):
    root = dummy_request.registry.root
    ch = ChangesetHandler(dummy_request.config, root, dummy_tmpdir)
    mocker.patch.object(ch, 'add_resource')
    ch.initialize()
    assert 4 == ch.add_resource.call_count


def test_changeset_add_resource(dummy_request, dummy_tmpdir):
    root = dummy_request.registry.root
    ch = ChangesetHandler(dummy_request.config, root, dummy_tmpdir)
    root: Root = dummy_request.registry.root
    target = dummy_tmpdir / Path('hello.md')
    ch.add_resource(target)
    hello: Resource = root['hello']
    assert 'Some Dummy Doc' == hello.title
