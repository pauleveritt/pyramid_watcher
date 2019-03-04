from pathlib import Path

from pyramid.config import Configurator
from pyramid.traversal import find_resource

from pyramid_watcher.models import Changeset
from .resources.root import Root
from .resources.processors import PROCESSORS

log = __import__('logging').getLogger(__name__)


class ChangesetHandler:
    def __init__(self, config: Configurator, root: Root, content_root: Path):
        self.config = config
        self.root = root
        self.content_root = content_root

    def add_resource(self, target: Path):
        """ Given a path from first-scan or changeset, add/replace in tree """

        extension = target.suffix[1:]
        processor = PROCESSORS[extension]

        # Use Pyramid's resource path functions to get the parent object
        # of this file.
        parent_path = '/' + str(target.parent.relative_to(self.content_root))
        parent = find_resource(self.root, parent_path)

        resource = processor(target, parent)
        if resource is not None:
            self.root[resource.__name__] = resource

    def initialize(self):
        """ Called at startup time, read all content into the resource tree """

        for target in self.content_root.glob('**/*.md'):
            self.add_resource(target)

    def __call__(self, changeset: Changeset):
        for change in changeset.changes:
            target = change.file_path
            self.add_resource(target)
