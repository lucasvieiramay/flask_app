from persons.models import Person, PersonSchema
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PersonService():

    def __init__(self):
        self.person_schema = PersonSchema()

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
                setattr(obj, field, params[field])
        db.session.commit()
        return self.person_schema.dump(obj).data

    def remove_obj(self, obj):
        if int(obj):
            obj = Person.query.get(obj)

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
