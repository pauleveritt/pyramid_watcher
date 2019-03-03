"""

Echo Demo

Simple demo to have one view which shows changes to files in the content
area.

"""

from pyramid.config import Configurator

from .resources import bootstrap, Root


def main(global_config, **settings):
    with Configurator(
            settings=settings,
            root_factory=bootstrap
    ) as config:
        config.include('pyramid_jinja2')
        config.include('pyramid_watcher')
        config.scan()

        # Stash an instance of the Root in the registry
        root = Root(title='Home Page')
        config.registry.root = root

        # Let the root handle changesets
        config.register_changehandler(root.handle_changeset)

    return config.make_wsgi_app()
