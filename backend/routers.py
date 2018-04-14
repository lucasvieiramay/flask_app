from flask import Flask, abort
from utils import default_response


app = Flask(__name__)


@app.route('/persons/list')
def person_list():
    data = ''
    response = default_response(data=data, status=200)
    return response


@app.route('/person/<int:person_id>')
def person_detail(book_id):
    data = ''
    # book = search_book(books, book_id)
    # if person is None:
    # abort(404)
    response = default_response(data=data, status=200)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
