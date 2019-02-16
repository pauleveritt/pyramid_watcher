from pyramid.config import Configurator

from .resources import bootstrap


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=bootstrap
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()
    return config.make_wsgi_app()
