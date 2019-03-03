from pyramid_watcher.samples.echo.handlers import ChangeHandler


def test_changelog_handler(dummy_request, dummy_changeset):
    ch = ChangeHandler(dummy_request.config)
    ch(dummy_changeset)
    siteroot = dummy_request.registry.siteroot
    first_changes = siteroot.changesets[0].changes
    assert '/path/added' == next(iter(first_changes)).file_path
