import os
from werkzeug.utils import secure_filename
from utils import allowed_file_upload
from persons.models import Person, PersonSchema
from flask_sqlalchemy import SQLAlchemy
from flask import abort
from validate_email import validate_email
from pycpfcnpj import cpfcnpj
from local_settings import UPLOAD_FOLDER


db = SQLAlchemy()


class PersonService():

    def __init__(self):
        self.person_schema = PersonSchema()

    def filter_objects(self, filter_field):
        list_obj = []
        if filter_field.get('name'):
            list_obj = Person().query_by_name(
                filter_field.get('name'))
        elif filter_field.get('email'):
            list_obj = Person().query_by_email(
                filter_field.get('email'))
        elif filter_field.get('birth_date'):
            list_obj = Person().query_by_birth_date(
                filter_field.get('birth_date'))
        elif filter_field.get('doc_id'):
            list_obj = Person().query_by_doc_id(
                filter_field.get('doc_id'))

        serialized_list = []
        for item in list_obj:
            serialized_list.append(
                self.person_schema.dump(item).data)
        return serialized_list

    def get_all_objects(self):
        list_obj = Person.query.all()
        person_schema = PersonSchema()
        serialized_list = []
        for item in list_obj:
            serialized_list.append(
                person_schema.dump(item).data)
        return serialized_list

    def add_obj(self, **params):
        if 'file' in params.keys():
            file = params['file']
            if file.filename == '':
                return False
            if file and allowed_file_upload(file.filename):
                # Check the size of the file
                # Save on tmp to check the size
                # And only after that really saves
                filename = secure_filename(file.filename)
                tmp_dir = '/tmp/{}'.format(filename)
                file.save(tmp_dir)
                size = os.stat(tmp_dir).st_size
                if size < 1e+6:
                    root_dir = os.path.dirname(os.path.abspath(__file__))
                    upload_dir = "{}{}/{}".format(
                        root_dir, UPLOAD_FOLDER, filename)
                    # The image has less then 1mb, lets move to the real folder
                    os.rename(tmp_dir, upload_dir)
                    # Add the image to save on obj
                    params['image'] = upload_dir

                # Remove file from params
                del params['file']

        db.session.close_all()
        obj = Person(**params)
        db.session.add(obj)
        db.session.commit()
        return self.person_schema.dump(obj).data

    def update_obj(self, **params):
        obj = Person.query.get(params['id'])
        for field in params.keys():
            if field != 'id' and params[field]:
                if field == 'doc_id':
                    duplicated = Person.query.filter(
                        Person.doc_id == params['doc_id'],
                        Person.id != params['id'])
                    if duplicated.all():
                        # Already has this num_id on our database
                        return False
                elif field == 'email':
                    duplicated = Person.query.filter(
                        Person.email == params['email'],
                        Person.id != params['id'])
                    if duplicated.all():
                        # Already has this email on our database
                        return False
                setattr(obj, field, params[field])
        db.session.commit()
        return self.person_schema.dump(obj).data

    def remove_obj(self, obj_id):
        obj = Person.query.filter_by(id=obj_id).first()
        if not obj:
            abort(404)
        if obj.image:
            self.delete_image(obj.image)
        # prevents the object from being used in another session
        db.session.close_all()
        db.session.delete(obj)
        db.session.commit()
        return True

    def delete_image(self, image):
        return os.remove(image)

    def validate_field(self, **params):
        required_fields = ['name', 'doc_id', 'email']
        if set(required_fields).issubset(params.keys()):
            if params['name'] and params['doc_id'] and params['email']:
                return True
        return False

    def set_parameters(self, form):
        params = {
            'name': form.get('name'),
            'doc_id': form.get('doc_id'),
            'birth_date': form.get('birth_date'),
            'email': form.get('email'),
        }
        file = form.get('file')
        if file:
            params['file'] = file

        if params['email']:
            # This check if the email has a smtp server, and he really exists
            # but made the apllication really slow
            # smtp_verify = validate_email(params['email'], verify=True)

            # This is a simple validador
            smtp_verify = validate_email(params['email'])
            if not smtp_verify:
                return 'fake_email'

        if params['doc_id']:
            valid_cpf = cpfcnpj.validate(params['doc_id'])
            if not valid_cpf:
                return 'fake_cpf'
        return params
