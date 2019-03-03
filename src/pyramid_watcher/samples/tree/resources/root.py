from collections import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from pyramid_watcher.models import Changeset
from .processors import PROCESSORS

log = __import__('logging').getLogger(__name__)


@dataclass
class Root(Mapping):
    title: str
    __name__ = ''
    __parent__: Optional[str] = None

    def __post_init__(self):
        """ Make this a dictionary-like object that can contain things """
        self._dict = {}

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def add_resource(self, target: Path, parent):
        """ Given a path from first-scan or changeset, add/replace in tree """

        extension = target.suffix[1:]
        processor = PROCESSORS[extension]
        resource = processor(target, parent)
        if resource is not None:
            parent[resource.__name__] = resource

    def handle_changeset(self, changeset: Changeset):

        for change in changeset.changes:
            target = Path(change.file_path)
            self.add_resource(target, self)

    def initialize(self, content_root: Path):
        """ Called at startup time, read all content into the resource tree """

        for target in content_root.glob('**/*.md'):
            self.add_resource(target, self)
