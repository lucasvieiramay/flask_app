import local_settings
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = local_settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = local_settings.DATABASE_URI

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello world'


@app.route('/list-persons', methods=['GET'])
def list_persons():
    pass


if __name__ == '__main__':
    app.run(debug=True)
