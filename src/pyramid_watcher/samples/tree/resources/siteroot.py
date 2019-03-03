from collections.abc import Mapping
from dataclasses import dataclass, field
from os import walk
from pathlib import Path
from typing import Optional, List

from pyramid_watcher.models import Changeset
from .processors import PROCESSORS

log = __import__('logging').getLogger(__name__)


@dataclass
class SiteRoot(Mapping):
    title: str
    changesets: List[Changeset] = field(default_factory=list)
    __name__: str = ''
    __parent__: Optional[str] = None

    def __post_init__(self):
        """ Make this a dictionary-like object that can contain things """
        self._dict = {}

    def __getitem__(self, key):
        return self._dict[key]

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def handle_changeset(self, changeset: Changeset):
        self.changesets.append(changeset)

    def initialize(self, content_root: str):
        """ Called at startup time, read all content into the resource tree """

        for (dirpath, dirs, files) in walk(content_root):
            for f in files:
                filename = Path(dirpath) / Path(f)
                extension = filename.suffix[1:]
                processor = PROCESSORS[extension]
                resource = processor(filename, content_root, self)
                self._dict[resource.__name__] = resource
