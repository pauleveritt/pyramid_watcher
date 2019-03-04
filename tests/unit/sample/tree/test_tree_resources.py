from pathlib import Path

from pyramid_watcher.samples.tree.resources.base_resources import Folder, Resource
from pyramid_watcher.samples.tree.resources.document import Document


def test_resources_root(dummy_root):
    assert 'Dummy Siteroot' == dummy_root.title


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
