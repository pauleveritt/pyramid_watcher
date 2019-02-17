"""

Wrap the watcher in a thread to run it in the background.

"""
from pathlib import Path
from threading import Thread, Lock
from time import sleep
from typing import Callable

from .watchgod_watcher import DefaultDirWatcher

log = __import__('logging').getLogger(__name__)


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
        self.enabled = False
        self.watcher = DefaultDirWatcher(str(watched_path))

    def run(self):
        while self.enabled:
            for changes in self.watcher.check():
                self.callback(changes)
            sleep(self.interval)

    def stop(self):
        self.enabled = False
