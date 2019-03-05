"""

Make some views available for things like SSE.

"""
import json

from pyramid.response import Response

log = __import__('logging').getLogger(__name__)

U_SSE_PAYLOAD = "id:{0}\nevent: new_request\ndata:{1}\n\n"

last_request_id = 9999
last_modified = 1


def livereload_view(request):
    global last_modified
    headers = [('Content-Type', 'text/event-stream'),
               ('Cache-Control', 'no-cache')
               ]
    log.info('In livereload_view')
    response = Response(headerlist=headers)

    data = dict(last_modified=last_modified)

    response.text = U_SSE_PAYLOAD.format(last_request_id,
                                         json.dumps(data))
    last_modified += 1
    return response
