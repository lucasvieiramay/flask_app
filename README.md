# Flask API

A rest api made using flask.

## Getting Started

To run this project you need to follow the instructions for the backend and frontend, and setup your database.

### Prerequisites for the backend

- Python3
- Postgres

### Installing Backend

First you need to clone this project
```
git clone git@github.com:lucasvieiramay/flask_app.git
```

Now entry on the project folder and type
```
cd backend
```

If you already have python3 instaled, create the virtual enviroment

```
virtualenv -p python3 venv
```

Install the requirements
```
pip install -r requirements.txt
```

Create your local_settings file, your can use vim or nano...

```
vim local_settings.py
```

Now paste this code into

```
POSTGRES = {
    'user': 'postgres',
    'pw': '123123',
    'db': 'flask_db',
    'host': 'localhost',
    'port': '5432',
}

UPLOAD_FOLDER = '/uploads'
```

Create your database with the correct user and password (The same you put on your local settings file)


Fire up the database
```
python manage.py db init
```

Run Migrations
```
python manage.py db migrate
```

Run Upgrates
```
python manage.py db upgrade
```

And finally type

```
python app.py
```

## Running the tests

app file
```
python -m unittest test_app
```
app service
```
python -m unittest persons.services.test_service
```

## Authors

* **Lucas May**  - [Lucas May](https://github.com/lucasvieiramay)
