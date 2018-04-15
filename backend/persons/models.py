from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    doc_id = db.Column(db.String(11), unique=True)  # CPF
    # picture = db.Column(db.LargeBinary)
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(120), unique=True)


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        fields = ('id', 'name', 'doc_id', 'birth_date', 'email')
