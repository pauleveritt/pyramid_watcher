"""

Wrap the watcher in a thread to run it in the background.

"""
from dataclasses import field
from datetime import datetime
from pathlib import Path
from threading import Thread, Lock
from time import sleep
from typing import Callable, Set

from dataclasses import dataclass

from .watchgod_watcher import DefaultDirWatcher, FileChangeInfo

log = __import__('logging').getLogger(__name__)


@dataclass(eq=True, frozen=True)
class ChangeSetEntry:
    change_type: FileChangeInfo
    file_path: str


@dataclass
class ChangeSet:
    timestamp: datetime
    changes: Set[ChangeSetEntry] = field(default_factory=set)


class ThreadRunner(Thread):
    def __init__(self,
                 callback: Callable,
                 watched_path: Path,
                 interval=1):
        super().__init__()
        self.callback = callback
        self.watched_path = watched_path
        self.interval = interval
        self.lock = Lock()
        self.enabled = True
        self.watcher = DefaultDirWatcher(str(watched_path))

    def run(self):
        while self.enabled:
            changes = self.watcher.check()
            if changes:
                timestamp = datetime.now()
                changeset = ChangeSet(timestamp=timestamp, changes={
                    ChangeSetEntry(change_type=i[0], file_path=i[1])
                    for i in changes
                })
                self.callback(changeset)
            sleep(self.interval)

    def stop(self):
        self.enabled = False
