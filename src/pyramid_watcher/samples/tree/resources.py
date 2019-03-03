from dataclasses import dataclass, field
from os import walk
from typing import Optional, List

from pyramid_watcher.models import Changeset

log = __import__('logging').getLogger(__name__)


@dataclass
class SiteRoot:
    title: str
    changesets: List[Changeset] = field(default_factory=list)
    __name__: str = ''
    __parent__: Optional[str] = None

    def handle_changeset(self, changeset: Changeset):
        self.changesets.append(changeset)

    def initialize(self, content_root: str):
        """ Called at startup time, read all content into the resource tree """

        for (dirpath, dirs, files) in walk(content_root):
            log.info('Blah')
            for filename in files:
                log.info('Found file:' + filename)
