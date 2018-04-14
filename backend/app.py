import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import default_response
from local_settings import POSTGRES


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    doc_id = db.Column(db.String(11), unique=True)  # CPF
    # picture = db.Column(db.LargeBinary)
    birth_date = db.Column(db.Date)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)


@app.route('/persons/list')
def person_list():
    data = Person.query.all()
    response = default_response(data=data, status=200)
    return response


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
