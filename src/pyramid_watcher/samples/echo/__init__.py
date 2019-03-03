"""

Echo Demo

Simple demo to have one view which shows changes to files in the content
area.

"""

from pyramid.config import Configurator

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
        siteroot = SiteRoot(title='Home Page')
        config.registry.siteroot = siteroot

        # Let the siteroot handle changesets
        config.register_changehandler(siteroot.handle_changeset)

    return config.make_wsgi_app()
