from pathlib import Path

from pyramid.events import ApplicationCreated, subscriber
from pyramid_watcher.threadrunner import ThreadRunner

log = __import__('logging').getLogger(__name__)


@subscriber(ApplicationCreated)
def start_threadrunner(event: ApplicationCreated):
    registry = event.app.registry

    # Get the directory to watch from the config settings
    content_root = Path(registry.settings.get('content_root'))

    # Get the change handler from the registry settings
    handler = registry.settings['pyramid_watcher_handler']

    # Make the watcher and put it in the registry
    watcher = ThreadRunner(handler, content_root)
    registry['watcher'] = watcher

    try:
        # Tell the watcher to start running
        watcher.start()
    except KeyboardInterrupt:
        log.info('Shutting down file watcher')
