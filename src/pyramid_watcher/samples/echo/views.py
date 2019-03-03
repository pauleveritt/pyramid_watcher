from pyramid.view import view_config
from pyramid_watcher.samples.echo.resources import Root


@view_config(context=Root, renderer='templates/root.jinja2')
def root(context: Root, request):
    return dict(
        project='Echo Sample',
        title=context.title,
        changesets=context.changesets
    )
