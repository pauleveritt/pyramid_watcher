from pyramid.config import Configurator
from pyramid_watcher.samples.echo.handlers import ChangeHandler

from .resources import bootstrap


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=bootstrap
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()

        # Make a custom change handler instance and register it
        ch = ChangeHandler(config)
        config.register_changehandler(ch)
    return config.make_wsgi_app()
