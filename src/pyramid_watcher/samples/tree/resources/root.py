from dataclasses import dataclass
from pathlib import Path

from pyramid_watcher.models import Changeset

from .processors import PROCESSORS
from .base_resources import Folder

log = __import__('logging').getLogger(__name__)


@dataclass
class Root(Folder):
    """ This is a special kind of folder with parent of none """

    @staticmethod
    def add_resource(target: Path, parent):
        """ Given a path from first-scan or changeset, add/replace in tree """

        extension = target.suffix[1:]
        processor = PROCESSORS[extension]
        resource = processor(target, parent)
        if resource is not None:
            parent[resource.__name__] = resource

    def handle_changeset(self, changeset: Changeset):

        for change in changeset.changes:
            target = change.file_path
            self.add_resource(target, self)

    def initialize(self, content_root: Path):
        """ Called at startup time, read all content into the resource tree """

        for target in content_root.glob('**/*.md'):
            self.add_resource(target, self)
