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

### Prerequisites for the frontend

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).


## Authors

* **Lucas May**  - [Lucas May](https://github.com/lucasvieiramay)
