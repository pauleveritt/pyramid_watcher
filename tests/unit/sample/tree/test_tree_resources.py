def test_resources_root(dummy_root):
    assert 'Dummy Siteroot' == dummy_root.title
    assert 0 == len(dummy_root.changesets)


def test_resources_root_changes(dummy_root, dummy_changeset):
    dummy_root.handle_changeset(dummy_changeset)
    first_changes = dummy_root.changesets[0].changes
    assert '/path/added' == next(iter(first_changes)).file_path
