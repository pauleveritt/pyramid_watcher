from dataclasses import dataclass, field
from typing import Optional, List

from pyramid_watcher.models import Changeset


@dataclass
class Root:
    title: str
    changesets: List[Changeset] = field(default_factory=list)
    __name__: str = ''
    __parent__: Optional[str] = None

    def handle_changeset(self, changeset: Changeset):
        self.changesets.append(changeset)


def bootstrap(request) -> Root:
    return request.registry.root
