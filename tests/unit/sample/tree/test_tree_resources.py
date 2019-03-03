from pathlib import Path

from pytest_toolbox import mktree


def test_resources_root(dummy_root):
    assert 'Dummy Siteroot' == dummy_root.title
    assert 0 == len(dummy_root.changesets)


def test_resources_root_changes(dummy_root, dummy_changeset):
    dummy_root.handle_changeset(dummy_changeset)
    first_changes = dummy_root.changesets[0].changes
    assert '/path/added' == next(iter(first_changes)).file_path


def test_resources_initialize(tmpdir, dummy_request, mocker):
    tree = {
        'hello.md': 'title: Hello Dummy Doc\n---\nYou are not *here*.',
        'foo': {
            'index.md': 'title: Folder Doc\n---\nYou are not *here*.',
            'about.md': 'title: Some Dummy Doc\n---\nWe are *here*.',
        }
    }
    mktree(tmpdir, tree)
    root = dummy_request.registry.root
    content_root = Path(str(tmpdir))
    # mocker.patch.object(root, 'initialize')
    root.initialize(content_root)
    # root.initialize.assert_called_with('foo')


    # - Make a tree
    # - Initialize
    # - Check that the mock was called N times with right stuff
