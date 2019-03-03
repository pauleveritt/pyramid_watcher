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
        root = Root(title='Home Page')
        config.registry.root = root

        # Tell the Root to do its initial scan
        content_root = Path(config.registry.settings['content_root'])
        root.initialize(content_root)

        # Let the root handle changesets
        config.register_changehandler(root.handle_changeset)

    return config.make_wsgi_app()
