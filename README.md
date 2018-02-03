# django_rest_framework_tutorial

My practices about [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/) and [Django Rest Framework 3.6.4 tutorial Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/).

## Installation

This Django Web app need a lot of Python extras packages, please execute the following command:

```bash
$ pip install -r requirements.txt --timeout 120
```

### Build the Django Web app DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
### Create Django Admin User

This Django Web app need a to create a Django Admin User, for access and manager the Admin interface, please execute the following command:

**Tip:** for this local installation use the user as **admin** and password as **password123**.

```bash
$ python manage.py createsuperuser --email admin@mail.com --username admin
Password: 
Password (again): 
Superuser created successfully.
```

## Run the Django Web app

You need to run the Django server, please execute the following command:

```bash
$ python manage.py runserver
```

- Open your web browser with the following URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and see the Django Web app.

- Open your web browser with the following URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) and see the Django Admin Interface, use the user **admin** and password **admin**.

**Tip:** PLEASE add two **groups**, two **users** and later add a user into a group.

### Testing the API

You have 2 API Rest for testing, now access to the APIs, both from the command-line, using tools like **curl**, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/3/",
        "username": "rocio",
        "email": "rociogonzalez@gmail.com",
        "groups": [
            "http://127.0.0.1:8000/groups/3/"
        ]
    },
    {
        "url": "http://127.0.0.1:8000/users/2/",
        "username": "leonardo",
        "email": "leonardo@gmail.com",
        "groups": [
            "http://127.0.0.1:8000/groups/2/"
        ]
    }
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@mail.com",
        "groups": [
            "http://127.0.0.1:8000/groups/1/"
        ]
    }
]
```

The previus command testing the **users** API Rest, for testing the **groups** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 htp://127.0.0.1:8000/groups/
[
    {
        "url": "http://127.0.0.1:8000/groups/2/",
        "name": "Plone"
    },
    {
        "url": "http://127.0.0.1:8000/groups/3/",
        "name": "Botana"
    }
]
```

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
- [Django Rest Framework 3.6.4 tutorial Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/).
