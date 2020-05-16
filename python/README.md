# pipenv

## From setting up pipenv to running flask web application

```bash
$ cd <repository root>/python
$ pip install --upgrade pip
$ pip install pipenv
$ pipenv --python 3.5 shell
(python) $ exit
$ python --version
Python 2.7.12
$ pipenv shell
(python) $ python --version
Python 3.5.2
(python) $ cat Pipfile
python_version = "3.5"
(python) $ python using-flask.py
...
ImportError: No module named 'flask'
(python) $ pipenv install flask
(python) python using-flask.py
flask imported
(python) # write proper flask app
(python) $ FLASK_APP=using-flask-template.py flask run  # localhost:5000
...
^C
(python) $ exit
```

## Usage

```bash
$ cd <repository root>/python
$ pipenv shell
(python) $ cd flask/
(python) $ source load-env.sh
(python) $ ./go url/p-url.py    # localhost:5000
...
^C
(python) $ exit
```
