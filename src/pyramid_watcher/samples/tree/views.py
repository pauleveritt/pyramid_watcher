from pyramid.view import view_config

from .resources.siteroot import SiteRoot
from .resources.document import Document

log = __import__('logging').getLogger(__name__)


@view_config(context=SiteRoot, renderer='templates/siteroot.jinja2')
def siteroot(context: SiteRoot, request):
    children = list(context.values())
    return dict(
        project='Tree Sample',
        context=context,
        children=children
    )


@view_config(context=Document, renderer='templates/document.jinja2')
def document(context: Document, request):
    return dict(
        project='Tree Sample',
        context=context
    )
