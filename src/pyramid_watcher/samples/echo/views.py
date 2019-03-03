from pyramid.view import view_config
from pyramid_watcher.samples.echo.resources import SiteRoot


@view_config(context=SiteRoot, renderer='templates/siteroot_view.jinja2')
def siteroot(context: SiteRoot, request):
    return dict(
        project='Echo Sample',
        title=context.title,
        changesets=context.changesets
    )
