from pyramid.view import view_config
from .resources.siteroot import SiteRoot


@view_config(context=SiteRoot, renderer='templates/siteroot_view.jinja2')
def homepage(context: SiteRoot, request):
    return dict(
        project='Tree Sample',
        title=context.title,
        changesets=context.changesets
    )
