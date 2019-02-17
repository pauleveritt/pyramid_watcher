from pyramid.config import Configurator

from .directives import ChangeHandler, register_changehandler


def includeme(config: Configurator):
    # Store a default change-callback in the registry settings,
    # which can be overridden with the directive defined later.
    config.registry.settings['pyramid_watcher_handler'] = ChangeHandler()

    config.scan('.subscribers')
    config.add_directive('handle_watchchanges',
                         register_changehandler)
