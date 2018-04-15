import os
from flask import Flask, abort, redirect, request
from local_settings import POSTGRES
from flask_sqlalchemy import SQLAlchemy
from persons.services import PersonService
from utils import default_response
from sqlalchemy import exc


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
        'name': request.form.get('name'),
        'doc_id': request.form.get('doc_id'),
        'birth_date': request.form.get('birth_date'),
        'email': request.form.get('email'),
    }
    if service.validade_field(**params):
        try:
            data = service.add_obj(**params)
            status_code = 200
        except exc.IntegrityError as err:
            status_code = 409
            data = 'Error: {}'.format(err)
    else:
        data = 'Error: The following fields are not ' \
               'nullable: name, doc_id, email'
        status_code = 400
    return default_response(data=data, status=status_code)


@app.route('/person/edit/<id>', methods=['PATCH'])
def person_edit(id):
    return 'sim'


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
