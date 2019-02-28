"""

Echo Demo

Simple demo to have one view which shows changes to files in the content
area.

"""

from pyramid.config import Configurator
from pyramid_watcher.samples.echo.handlers import ChangeHandler

from .resources import bootstrap, SiteRoot


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=bootstrap
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()

        # Stash an instance of the SiteRoot in the registry
        site_root = SiteRoot(title='Home Page')
        config.registry.site_root = site_root

        # Make a custom change handler instance and register it
        ch = ChangeHandler(config)
        config.register_changehandler(ch)
    return config.make_wsgi_app()
