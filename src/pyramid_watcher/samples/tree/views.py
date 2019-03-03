from pyramid.view import view_config

from .resources.root import Root
from .resources.document import Document

log = __import__('logging').getLogger(__name__)


@view_config(context=Root, renderer='templates/root.jinja2')
def root(context: Root, request):
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
