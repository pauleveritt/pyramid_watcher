"""

Dataclasses as models (or vice versa)

We have a number of dataclasses used as type hints. Let's move
here to avoid circular references.

"""

from datetime import datetime
from dataclasses import dataclass, field
from typing import Set

from pyramid_watcher.watchgod_watcher import FileChangeInfo


@dataclass(eq=True, frozen=True)
class ChangesetEntry:
    """ One changed file entry in a changeset """

    change_type: FileChangeInfo
    file_path: str


@dataclass(frozen=True)
class Changeset:
    """ A collection of filesystem changes during an interval """

    timestamp: datetime
    changes: Set[ChangesetEntry] = field(default_factory=set)
