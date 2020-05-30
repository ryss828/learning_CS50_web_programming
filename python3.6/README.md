# python 3.6

## From setting up pipenv to running flask web application

The following was written when I set up pipenv for python 3.5.

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

## General Usage

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

## Learning

- Flask functions can return a simple string, html, or `render_template()`
- Templates can be fed variables via `render_template()`. Variables can be referenced in templates using 'double curly brackets'
- Templates can have Jinja2 controls like 'curly bracket percent if'
- Template inheritance is like *template method* in Design Pattern. Templates can inherit a base template
- `@app.route` specifies a url and allowed methods against the url
- Flask's `request` have `form` that the client submitted
- `form` tag specifies
  - url as a target using `action` attribute
  - http method using `method` attribute
- http methods need to be all capital letters in code e.g. POST
- Learn about ['The "Confirm Form Resubmission" Problem'](https://khalidabuhakmeh.com/solving-the-confirm-form-resubmission-problem) because it happens `python/flask/post-note/` when refreshing the page after POSTing the form.
- Every time a module is needed, do `pipenv install <module name>`. So if the code says 'from flask_session import ...' then do `pipenv install flask_session`

## New technology

- Python 3
- pipenv
- flask
- Django
