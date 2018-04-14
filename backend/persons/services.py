from persons.models import Person
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


class PersonService():

    def add_obj(**params):
        obj = Person(**params)
        db.session.add(obj)
        db.session.commit()
        return obj

    def remove_obj(obj):
        if int(obj):
            obj = Person.query.get(obj)

        db.session.delete(obj)
        db.session.commit()
        return True
