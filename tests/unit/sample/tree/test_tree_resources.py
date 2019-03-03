from pathlib import Path

from pyramid_watcher.samples.tree.resources.document import Document


def test_resources_root(dummy_root):
    assert 'Dummy Siteroot' == dummy_root.title


def test_resources_initialize(dummy_request, dummy_tmpdir, mocker):
    root = dummy_request.registry.root
    mocker.patch.object(root, 'add_resource')
    root.initialize(dummy_tmpdir)
    assert 4 == root.add_resource.call_count


def test_resources_add_resource(dummy_request, dummy_tmpdir):
    root = dummy_request.registry.root
    target = dummy_tmpdir / Path('hello.md')
    root.add_resource(target, root)
    hello: Document = root['hello']
    assert 'Some Dummy Doc' == hello.title

