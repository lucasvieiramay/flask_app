from persons.models import Person, PersonSchema
from flask_sqlalchemy import SQLAlchemy
from flask import abort

db = SQLAlchemy()


class PersonService():

    def __init__(self):
        self.person_schema = PersonSchema()

    def filter_objects(self, **params):
        list_obj = Person.query.filter(**params)
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
        return params

    def get_filters(self, request):
        filters = {}
        name = request.args.get('name')
        if name:
            filters['name'] = name
        num_id = request.args.get('num_id')
        if num_id:
            filters['num_id'] = num_id
        birth_date = request.args.get('birth_date')
        if birth_date:
            filters['birth_date'] = birth_date
        email = request.args.get('email')
        if email:
            filters['email'] = email
        return filters
