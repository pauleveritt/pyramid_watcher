from pyramid.config import Configurator

from pyramid_watcher.models import Changeset
from pyramid_watcher.samples.echo.resources import SiteRoot

log = __import__('logging').getLogger(__name__)


class ChangeHandler:
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changeset: Changeset):
        root: SiteRoot = self.config.registry.siteroot
        root.handle_changeset(changeset)
