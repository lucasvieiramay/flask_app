from persons.models import Person, PersonSchema
from flask_sqlalchemy import SQLAlchemy
from flask import abort
from validate_email import validate_email
from pycpfcnpj import cpfcnpj

db = SQLAlchemy()


class PersonService():

    def __init__(self):
        self.person_schema = PersonSchema()

    def filter_objects(self, filter_field):
        list_obj = []
        if filter_field.get('name'):
            name = '%{}%'.format(filter_field.get('name'))
            list_obj = Person.query.filter(
                Person.name.ilike(name)).all()
        elif filter_field.get('email'):
            email = '%{}%'.format(filter_field.get('email'))
            list_obj = Person.query.filter(Person.email.ilike(email)).all()
        elif filter_field.get('birth_date'):
            list_obj = Person.query.filter(
                Person.birth_date == filter_field.get('birth_date')).all()
        elif filter_field.get('doc_id'):
            list_obj = Person.query.filter(
                Person.birth_date == filter_field.get('doc_id')).all()

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

    def remove_obj(self, obj):
        if int(obj):
            obj = Person.query.filter_by(id=obj).first()
            if not obj:
                abort(404)
        # prevents the object from being used in another session
        db.session.close_all()
        db.session.delete(obj)
        db.session.commit()
        return True

    def validade_field(self, **params):
        if 'name' and 'doc_id' and 'email' in params.keys():
            return True
        return False

    def set_parameters(self, request):
        params = {
            'name': request.form.get('name'),
            'doc_id': request.form.get('doc_id'),
            'birth_date': request.form.get('birth_date'),
            'email': request.form.get('email'),
        }

        # This check if the email has a smtp server, and he really exists
        # but made the apllication really slow
        # smtp_verify = validate_email(params['email'], verify=True)

        # This is a simple validador
        smtp_verify = validate_email(params['email'])
        if not smtp_verify:
            return 'fake_email'

        valid_cpf = cpfcnpj.validate(params['doc_id'])
        if not valid_cpf:
            return 'fake_cpf'
        return params
