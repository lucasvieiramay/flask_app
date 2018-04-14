from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    doc_id = db.Column(db.String(11), unique=True)  # CPF
    # picture = db.Column(db.LargeBinary)
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(120), unique=True)
