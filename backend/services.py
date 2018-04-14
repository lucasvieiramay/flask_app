from app import Person


class PersonService():

    def get_all_objects(self):
        list_obj = Person.query.all()
        return list_obj

    def add_obj(self, **params):
        obj = Person(**params)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update_obj(self, **params):
        obj = Person.query.get(params['id'])
        for field in params.keys():
            if field != 'id':
                obj.field = params[field]
        db.session.commit()
        return obj

    def remove_obj(self, obj):
        if int(obj):
            obj = Person.query.get(obj)

        db.session.delete(obj)
        db.session.commit()
        return True
