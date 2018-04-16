import json
from flask import Response


JSON_MIME_TYPE = 'application/json'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def default_response(data='', status=200, headers=None):
    return Response(
        json.dumps(data), status, mimetype=JSON_MIME_TYPE)


def allowed_file_upload(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
