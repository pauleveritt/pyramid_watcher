from typing import Callable

from pyramid.config import Configurator

from .models import Changeset

log = __import__('logging').getLogger(__name__)


class ChangeHandler:
    """ Simple implementation to log when filesystem changes occur """
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changes: Changeset):
        log.info('Changes: ' + str(changes))


def register_changehandler(config: Configurator, handler: Callable):
    """ Stash the callable in the config """

    config.registry.change_handler = handler
