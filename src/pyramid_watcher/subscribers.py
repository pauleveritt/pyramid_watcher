from pathlib import Path

from pyramid.events import ApplicationCreated
from pyramid_watcher.threadrunner import ThreadRunner

log = __import__('logging').getLogger(__name__)


def start_threadrunner(event: ApplicationCreated):
    """ Event handler to run at startup time to fire up a watcher """
    registry = event.app.registry
    settings = registry.settings

    # Get watch_interval integer from settings. If not there, don't do
    # any watching.
    watch_interval = settings.get('watch_interval')
    if watch_interval is None:
        return

    # Get the directory to watch from the config settings
    content_root = Path(settings.get('content_root'))

    # Get the change handler from the registry settings
    handler = registry.change_handler

    # Make the watcher and put it in the registry
    watcher = ThreadRunner(handler, content_root, interval=int(watch_interval))
    registry.watcher = watcher

    try:
        # Tell the watcher to start running
        watcher.start()
    except KeyboardInterrupt:
        log.info('Shutting down file watcher')
