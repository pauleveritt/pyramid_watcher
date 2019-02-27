from pyramid.config import Configurator
from pyramid.events import ApplicationCreated
from pyramid_watcher.subscribers import start_threadrunner

from .directives import ChangeHandler, register_changehandler


def includeme(config: Configurator):
    # The ChangeHandler is a configurable callback run when there is a
    # new Changeset. There should only be one. A default is provided
    # but it can be overridden with the directive.
    ch = ChangeHandler(config)
    config.registry.settings['pyramid_watcher_handler'] = ch
    config.add_directive('register_changehandler', register_changehandler)

    # The Threadrunner watches changes on disk and calls the callback.
    # Subscribe to ApplicationCreated to start the
    # threadrunner as late as possible
    config.add_subscriber(start_threadrunner, ApplicationCreated)
