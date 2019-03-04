from pyramid.config import Configurator

from pyramid_watcher.models import Changeset
from pyramid_watcher.samples.tree.resources.root import Root

log = __import__('logging').getLogger(__name__)


class ChangesetHandler:
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changeset: Changeset):
        root: Root = self.config.registry.root
        for change in changeset.changes:
            target = change.file_path
            root.add_resource(target)
