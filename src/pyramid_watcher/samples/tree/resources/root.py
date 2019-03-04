from dataclasses import dataclass
from pathlib import Path

from .base_resources import Folder
from .processors import PROCESSORS

log = __import__('logging').getLogger(__name__)


@dataclass
class Root(Folder):
    """ This is a special kind of folder with parent of none """

    def add_resource(self, target: Path):
        """ Given a path from first-scan or changeset, add/replace in tree """

        extension = target.suffix[1:]
        processor = PROCESSORS[extension]
        resource = processor(target, self)
        if resource is not None:
            self[resource.__name__] = resource

    def initialize(self, content_root: Path):
        """ Called at startup time, read all content into the resource tree """

        for target in content_root.glob('**/*.md'):
            self.add_resource(target)
