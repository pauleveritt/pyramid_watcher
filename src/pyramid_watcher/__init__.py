from pyramid.config import Configurator

from .directives import ChangeHandler, register_changehandler


def includeme(config: Configurator):
    # Store a default change-callback in the registry settings,
    # which can be overridden with the directive defined later.
    # The change handler will need access to the config, so pass
    # it into the constructor.
    ch = ChangeHandler(config)
    config.registry.settings['pyramid_watcher_handler'] = ch

    config.scan('.subscribers')
    config.add_directive('register_changehandler',
                         register_changehandler)
