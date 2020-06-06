# Django

[Django - Lecture 3 - CS50's Web Programming with Python and JavaScript 2020](https://www.youtube.com/watch?v=w8q0C-C1js4&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=5)

## Set-up

1. **Installing Django:** `pipenv install django==3.0`
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
12. **Creating Django project:** `django-admin startproject django-lecture3`
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

14. `cd djangolecture3/`
15. Ran Django server `python manage.py runserver`
16. **Creating an app in the project:** `python manage.py startapp hello`
17. The tree is:

    ```bash
    djangolecture3/
    ├── djangolecture3
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── hello
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── README.md
    ```

18. Add `hello` entry in `INSTALLED_APPS` in `djangolecture3/djangolecture3/settings.py`
19. Add function that handles http request in `djangolecture3/hello/views.py`
20. Add `djangolecture3/hello/urls.py` for the app
21. Link global `url.py` to hello app's `url.py` by adding an entry in `djangolecture3/djangolecture3/urls.py`
22. `cd djangolecture3; python manage.py runserver`
23. Put in `http://localhost:8000/hello/` and see `Hello World!`

## Learning

- Django project comprises multiple apps
- When pylint complains 'Unable to import...' in VS Code: Solution: open VS Code from an activated virtual environment
  - Open the terminal window
  - Activate the relevant python virtual environment
  - Ensure Pylint is installed within this virtual environment `pipenv install pylint`
  - Close all instances of VS Code
  - Launch VS Code from within this terminal window (this will ensure the VS Code process will inherit all of the Virtual Env environment settings)
  - If VS Code does not choose the right Python version, choose the correct pipenv one
  - Now the 'Unable to import' errors are gone
- An app has `url.py` and `views.py`
  - `url.py` maps urls and functions that are defined in `views.py`
  - `views.py` defines functions that return either `HttpResponse` or `render()` taking templates
- Rendering templates
  - `view.py` defines function that returns `render()`, in which a template (i.e. html) can be specified e.g. `return render(request, "hello/rend_temp.html")`
  - This arg is the path under `<app>/tempaltes/` directory.

    ```bash
    $ tree hello
    hello/
    ..
    ├── templates/
    │   └── hello/
    │       └── rend_temp.html
    ├── urls.py
    └── views.py
    ```

- Templates can be fed variables. To do so, pass a dictionary to `render()` as a 3rd argument like so:

  ```python
  return render(request, "hello/rend_temp2.html", {
      "name": someone.capitalize()
  })
  ```

  Use the variables with `{{ }}` in templates.
