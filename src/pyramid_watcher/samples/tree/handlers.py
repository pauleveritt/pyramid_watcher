from pathlib import Path

from pyramid.config import Configurator

from pyramid_watcher.models import Changeset
from .resources.root import Root
from .resources.processors import PROCESSORS

log = __import__('logging').getLogger(__name__)


class ChangesetHandler:
    def __init__(self, config: Configurator):
        self.config = config
        self.root: Root = config.registry.root

    def add_resource(self, target: Path):
        """ Given a path from first-scan or changeset, add/replace in tree """

        extension = target.suffix[1:]
        processor = PROCESSORS[extension]
        resource = processor(target, self.root)
        if resource is not None:
            self.root[resource.__name__] = resource

    def initialize(self, content_root: Path):
        """ Called at startup time, read all content into the resource tree """

        for target in content_root.glob('**/*.md'):
            self.add_resource(target)

    def __call__(self, changeset: Changeset):
        for change in changeset.changes:
            target = change.file_path
            self.add_resource(target)
