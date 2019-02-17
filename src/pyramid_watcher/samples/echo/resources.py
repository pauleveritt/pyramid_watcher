from dataclasses import dataclass, field
from typing import Optional, List

from pyramid_watcher.watchgod_watcher import FileChangeInfo


@dataclass
class ChangeSet:
    change_type: FileChangeInfo
    file_path: str


@dataclass
class SiteRoot:
    title: str
    changesets: List[ChangeSet] = field(default_factory=list)
    __name__: str = ''
    __parent__: Optional[str] = None

    def handle_changeset(self, changeset=List[ChangeSet]):
        self.changesets.append(changeset)


def bootstrap(request):
    return request.registry.site_root
