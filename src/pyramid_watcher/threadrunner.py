"""

Wrap the watcher in a thread to run it in the background.

"""
from datetime import datetime
from pathlib import Path
from threading import Thread, Lock
from time import sleep
from typing import Callable

from .models import Changeset, ChangesetEntry
from .watchgod_watcher import DefaultDirWatcher

log = __import__('logging').getLogger(__name__)


class ThreadRunner(Thread):
    """ Run a watcher in a thread """
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
                changeset = Changeset(timestamp=timestamp, changes={
                    ChangesetEntry(change_type=i[0], file_path=i[1])
                    for i in changes
                })
                self.callback(changeset)
            sleep(self.interval)

    def stop(self):
        self.enabled = False
