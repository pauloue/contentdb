# Content Database

## Setup

First create a Python virtual env:

	virtualenv env -ppython3
	source env/bin/activate

then use pip:

	pip3 install -r requirements.txt

### Development

* Copy config.example.cfg to config.cfg
* Fill SECRET_KEY and WTF_CSRF_SECRET_KEY in with a random string
* Make a Github OAuth Client at <https://github.com/settings/developers>:
	* Homepage URL - `http://localhost:5000/`
	* Authorization callback URL - `http://localhost:5000/user/github/callback/`
* Put client id and client secret in GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET
* Setup the database: python3 setup.py


## Running

### Development

You need to enter the virtual environment if you haven't yet in
the current session:

	source env/bin/activate

If you need to, reset the db like so:

	python3 setup.py -t

Then run the server:

	./rundebug.py

Then view in your web browser: http://localhost:5000/

## How-tos

### Start celery worker

```sh
FLASK_CONFIG=../config.cfg celery -A app.tasks.celery worker
```

### Create migration

```sh
# if sqlite
python setup.py -t
rm db.sqlite && python setup.py -t && FLASK_CONFIG=../config.cfg FLASK_APP=app/__init__.py flask db stamp head

# Create migration
FLASK_CONFIG=../config.cfg FLASK_APP=app/__init__.py flask db migrate

# Run migration
FLASK_CONFIG=../config.cfg FLASK_APP=app/__init__.py flask db upgrade
```
