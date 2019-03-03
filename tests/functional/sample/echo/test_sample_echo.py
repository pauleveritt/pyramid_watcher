from datetime import datetime

from bs4 import BeautifulSoup
from pyramid_watcher.models import Changeset, ChangesetEntry
from pyramid_watcher.samples.echo import SiteRoot
from pyramid_watcher.watchgod_watcher import FileChangeInfo
from pytest import fixture


@fixture
def dummy_changeset() -> Changeset:
    now = datetime.now()
    ce = ChangesetEntry(FileChangeInfo.added, '/path/added')
    cs = Changeset(now, {ce})
    return cs


def test_functional_home(testapp):
    soup: BeautifulSoup = testapp.get('/', status=200).html
    assert 'Home Page - Echo Sample' == soup.select_one('title').get_text().strip()
    assert 'Home Page' == soup.select_one('h1.title').get_text().strip()
    assert 'Changesets' == soup.select_one('h4').get_text().strip()


def test_functional_home_changesets(testapp, dummy_changeset):
    # Broadcast some changes, see if picked up
    siteroot: SiteRoot = testapp.app.registry.siteroot

    # First, ensure no entries
    soup: BeautifulSoup = testapp.get('/', status=200).html
    assert 0 == len(soup.select('li.changeset'))

    # Broadcast then try again
    siteroot.handle_changeset(dummy_changeset)
    soup: BeautifulSoup = testapp.get('/', status=200).html
    assert 1 == len(soup.select('li.changeset'))
