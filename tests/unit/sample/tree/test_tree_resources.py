from pathlib import Path

from pyramid_watcher.samples.tree.resources.document import Document
from pyramid_watcher.samples.tree.resources.base_resources import Folder, Resource


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
    root.add_resource(target)
    hello: Document = root['hello']
    assert 'Some Dummy Doc' == hello.title


def test_base_resources_resource(dummy_request):
    root = dummy_request.registry.root
    r = Resource(name='hello', parent=root, title='Hello')
    assert 'hello' == r.__name__
    assert root == r.__parent__
    assert 'Hello' == r.title


def test_base_resources_folder(dummy_request):
    root = dummy_request.registry.root
    parent = Folder(name='parent', parent=root, title='Hello')
    r = Folder(name='hello', parent=parent, title='Hello')
    parent[r.__name__] = r

    assert 'hello' == parent[r.__name__].__name__
    assert parent == parent[r.__name__].__parent__
    assert 'Hello' == parent[r.__name__].title

    assert 1 == len(parent)
    assert 'hello' in parent
    del parent['hello']
    assert 0 == len(parent)
