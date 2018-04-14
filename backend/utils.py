import json
from flask import Response

JSON_MIME_TYPE = 'application/json'


def default_response(data='', status=200, headers=None):
    return Response(
        json.dumps(data), status, mimetype=JSON_MIME_TYPE)
