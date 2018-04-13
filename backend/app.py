from local_settings import *
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

# TODO: Find a way to insert this into another file
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route('/')
def index():
    return 'hello world'

@app.route('/list-persons', methods=['GET'])
def list_persons():
    pass

if __name__ == '__main__':
    app.run(debug=True)

