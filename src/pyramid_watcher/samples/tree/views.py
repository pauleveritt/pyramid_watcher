from pyramid.view import view_config
from .resources.siteroot import SiteRoot

log = __import__('logging').getLogger(__name__)


@view_config(context=SiteRoot, renderer='templates/siteroot_view.jinja2')
def homepage(context: SiteRoot, request):
    return dict(
        project='Tree Sample',
        context=context,
        children=context.values()
    )
