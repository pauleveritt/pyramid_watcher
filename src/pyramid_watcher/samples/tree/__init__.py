"""

Resource Tree Sample

More of a full-featured demo of using directories of files as a tree
of resources. This example:

- Loads all the files into the resource tree at startup

- As changesets come in, update the resource tree.

"""

from pyramid.config import Configurator
from pyramid.request import Request

from .resources.siteroot import SiteRoot


def root_factory(request: Request):
    return request.registry.siteroot


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=root_factory
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()

        # Stash an instance of the SiteRoot in the registry
        siteroot = SiteRoot(title='Home Page')
        config.registry.siteroot = siteroot

        # Tell the SiteRoot to do its initial scan
        siteroot.initialize(config.registry.settings['content_root'])

        # Let the siteroot handle changesets
        config.register_changehandler(siteroot.handle_changeset)

    return config.make_wsgi_app()
