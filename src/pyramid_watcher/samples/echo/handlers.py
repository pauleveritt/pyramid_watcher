from pyramid.config import Configurator

log = __import__('logging').getLogger(__name__)


class ChangeHandler:
    def __init__(self, config: Configurator):
        self.config = config

    def __call__(self, changes):
        log.info('Custom Changes: ' + str(changes))
