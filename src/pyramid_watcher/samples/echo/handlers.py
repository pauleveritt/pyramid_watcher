from typing import List

from pyramid.config import Configurator
from pyramid_watcher.samples.echo.resources import ChangeSet

log = __import__('logging').getLogger(__name__)


class ChangeHandler:
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changeset: List[ChangeSet]):
        # TODO Got into a circular reference, quick fix as local
        from pyramid_watcher.samples.echo import SiteRoot
        root: SiteRoot = self.config.registry.site_root
        root.handle_changeset(changeset)
