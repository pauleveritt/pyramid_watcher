from typing import Callable

from pyramid.config import Configurator
from pyramid_watcher.threadrunner import ChangeSet

log = __import__('logging').getLogger(__name__)


class ChangeHandler:
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changes: ChangeSet):
        log.info('Changes: ' + str(changes))


def register_changehandler(config: Configurator, handler: Callable):
    """ Stash the callable in the config """
    config.registry.settings['pyramid_watcher_handler'] = handler
