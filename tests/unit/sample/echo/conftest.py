from datetime import datetime

from pytest import fixture
from pyramid.testing import DummyRequest, DummyResource, setUp, tearDown

from pyramid_watcher.models import Changeset, ChangesetEntry
from pyramid_watcher.watchgod_watcher import FileChangeInfo

from pyramid_watcher.samples.echo.resources import SiteRoot


@fixture
def dummy_siteroot() -> SiteRoot:
    yield SiteRoot(title='Dummy Siteroot')


@fixture
def dummy_changeset() -> Changeset:
    now = datetime.now()
    ce = ChangesetEntry(FileChangeInfo.added, '/path/added')
    cs = Changeset(now, {ce})
    return cs


@fixture
def dummy_request(dummy_siteroot) -> DummyRequest:
    dummy_request = DummyRequest()
    config = setUp(request=dummy_request)
    dummy_request.registry.siteroot = dummy_siteroot
    dummy_request.config = config
    yield dummy_request
    tearDown()


@fixture
def dummy_context() -> DummyResource:
    yield DummyResource(title='Dummy Title')