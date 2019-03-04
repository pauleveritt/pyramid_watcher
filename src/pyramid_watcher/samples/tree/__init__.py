"""

Resource Tree Sample

More of a full-featured demo of using directories of files as a tree
of resources. This example:

- Loads all the files into the resource tree at startup

- As changesets come in, update the resource tree.

"""

from pathlib import Path

from pyramid.config import Configurator
from pyramid.request import Request

from .handlers import ChangesetHandler
from .resources.root import Root


def root_factory(request: Request):
    return request.registry.root


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=root_factory
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()

        # Stash an instance of the Root in the registry
        root = Root(name='', parent=None, title='Home Page')
        config.registry.root = root

        # Get the path to the content root
        content_root = Path(config.registry.settings['content_root'])

        # Make a custom change handler instance and register it
        ch = ChangesetHandler(config, root, content_root)
        config.register_changehandler(ch)

        # Now initialize
        ch.initialize()

    return config.make_wsgi_app()
