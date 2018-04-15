import os
from flask import Flask, abort, redirect, request
from local_settings import POSTGRES
from flask_sqlalchemy import SQLAlchemy
from persons.services import PersonService
from utils import default_response


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
db.init_app(app)


@app.route('/persons/list', methods=['GET'])
def person_list():
    service = PersonService()
    data = service.get_all_objects()
    response = default_response(data=data, status=200)
    return response


@app.route('/person/add', methods=['POST'])
def person_add():
    service = PersonService()
    params = {
        'name': request.args.get('name'),
        'doc_id': request.args.get('doc_id'),
        'birth_date': request.args.get('birth_date'),
        'email': request.args.get('email'),
    }
    person = service.add_obj(**params)
    return default_response(data=person, status=200)


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
