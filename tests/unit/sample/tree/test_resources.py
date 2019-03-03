def test_siteroot(dummy_siteroot):
    assert 'Dummy Siteroot' == dummy_siteroot.title
    assert 0 == len(dummy_siteroot.changesets)


def test_siteroot_changes(dummy_siteroot, dummy_changeset):
    dummy_siteroot.handle_changeset(dummy_changeset)
    first_changes = dummy_siteroot.changesets[0].changes
    assert '/path/added' == next(iter(first_changes)).file_path
