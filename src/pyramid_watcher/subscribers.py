from pathlib import Path

from pyramid.events import ApplicationCreated, subscriber
from pyramid_watcher.threadrunner import ThreadRunner

log = __import__('logging').getLogger(__name__)


def watcher_handler(changes):
    log.info('Changes to files: ' + str(changes))


@subscriber(ApplicationCreated)
def start_threadrunner(event: ApplicationCreated):
    registry = event.app.registry

    # Get the directory to watch from the config settings
    content_root = Path(registry.settings.get('content_root'))

    # Make the watcher and put it in the registry
    handler = watcher_handler
    watcher = ThreadRunner(handler, content_root)
    registry['watcher'] = watcher

    try:
        # Tell the watcher to start running
        watcher.start()
    except KeyboardInterrupt:
        log.info('Shutting down file watcher')
