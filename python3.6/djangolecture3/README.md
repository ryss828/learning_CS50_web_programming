# Django

[Django - Lecture 3 - CS50's Web Programming with Python and JavaScript 2020](https://www.youtube.com/watch?v=w8q0C-C1js4&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=5)

## Set-up

1. Tried to install django: `pipenv install django==3.0`
2. Got error saying python needs to be >= 3.6 (python in pipenv that I was using was 3.5)
3. Installed python 3.6 globally in Ubuntu
4. Copied `python/` to `python3.6/`; `cd python3.6/`
5. Removed `Pipfile.lock` (?)
6. `pipenv --python 3.6 shell`
7. Got warning 'Pipfile requires python 3.5'
8. Either changed it to 3.6 or deleted the line, probably changed it
9. Created `Pipfile.lock` by `pipenv lock` # Generates Pipfile.lock
10. Just ran `pipenv sync` # Installs all packages specified in Pipfile.lock
11. Installed Django `pipenv install django==3.0`
12. Created Django project `django-admin startproject django-lecture3`
13. Now the dir tree is:

    ```bash
    djangolecture3/
    ├── djangolecture3
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── README.md
    ```

1. `cd djangolecture3/`
2. Ran Django server `python manage.py runserver`

## Learning
