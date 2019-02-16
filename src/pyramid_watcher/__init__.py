from importlib import resources

from pathlib import Path

from pyramid_watcher.threadrunner import ThreadRunner

log = __import__('logging').getLogger(__name__)


def watcher_handler(changes):
    log.info('Changes to files: ' + str(changes))


def includeme(config):
    # Make the watcher and put it in the registry
    handler = watcher_handler
    dir_to_watch = Path('../../../../docs')
    watcher = ThreadRunner(handler, dir_to_watch)
    config.registry['watcher'] = watcher

    try:
        # Tell the watcher to start running
        watcher.run()
    except KeyboardInterrupt:
        log.info('Shutting down file watcher')
