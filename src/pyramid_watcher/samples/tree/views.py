import json
from calendar import timegm
from datetime import datetime

from pyramid.response import Response
from pyramid.view import view_config

from .handlers import ChangesetHandler
from .resources.document import Document
from .resources.root import Root

log = __import__('logging').getLogger(__name__)

RETRY_INTERVAL = 500
SSE_PAYLOAD = "event: new_request\nretry: {0}\ndata:{1}\n\n"


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


def livereload_view(request):
    headers = [('Content-Type', 'text/event-stream'),
               ('Cache-Control', 'no-cache')
               ]
    ch: ChangesetHandler = request.registry.change_handler
    response = Response(headerlist=headers)

    last_modified = timegm(datetime.timetuple(ch.last_modified))
    data = dict(last_modified=last_modified)

    response.text = SSE_PAYLOAD.format(RETRY_INTERVAL, json.dumps(data))
    return response
