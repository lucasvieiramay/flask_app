import os
from flask import Flask, request
from flask_cors import CORS
from flask import send_file
from flask_sqlalchemy import SQLAlchemy
from local_settings import POSTGRES, UPLOAD_FOLDER
from persons.services import PersonService
from utils import default_response
from sqlalchemy import exc
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
db.init_app(app)


@app.route('/persons/list', methods=['GET'])
def person_list():
    service = PersonService()
    filter_field = request.args
    if not filter_field:
        data = service.get_all_objects()
    else:
        data = service.filter_objects(filter_field)

    response = default_response(data=data, status=200)
    return response


@app.route('/person/add', methods=['POST'])
def person_add():
    service = PersonService()
    params = service.set_parameters(request.form)
    if params == 'fake_email':
        data = "Email not valid"
        status_code = 401
    elif params == 'fake_cpf':
        data = "CPF or CNPJ not valid"
        status_code = 401
    elif service.validate_field(**params):
        try:
            if 'file' in request.files:
                params['file'] = request.files['file']
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
    status_code = 200
    service = PersonService()
    params = service.set_parameters(request.form)
    if params == 'fake_email':
        data = "Email not valid"
        status_code = 401
    elif params == 'fake_cpf':
        data = "CPF or CNPJ not valid"
        status_code = 401
    else:
        params['id'] = id
        data = service.update_obj(**params)
        if not data:
            data = 'Error: One of the following ' \
                'fields are duplicated: name, doc_id, email'
            status_code = 409
    return default_response(data=data, status=status_code)


@app.route('/person/remove/<person_id>', methods=['DELETE'])
def person_remove(person_id):
    service = PersonService()
    service.remove_obj(person_id)
    return default_response(data='Object removed', status=200)


@app.route('/person/image/<filename>', methods=['GET'])
def render_image(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    filename = secure_filename(filename)
    img_dir = "{}{}{}/{}".format(
        root_dir, '/persons/', UPLOAD_FOLDER, filename)

    return send_file(img_dir, mimetype='image/jpeg')


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
