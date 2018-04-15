from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(
        db.String(120), unique=True, nullable=False)
    doc_id = db.Column(
        db.String(11), unique=True, nullable=False)  # CPF
    name = db.Column(
        db.String(150), unique=False, nullable=False)
    birth_date = db.Column(db.Date, unique=False)
    deleted = db.Column(db.Boolean, default=False)


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        fields = ('id', 'name', 'doc_id', 'birth_date', 'email')
