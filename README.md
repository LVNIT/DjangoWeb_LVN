# Shoes Shop( Built with Django Framework )

## Stack
  - Python 3.8
  - Django 3.
  - mysqlclient
  
## Setup for develop

- Requirement Python 3.7+
- Create a Python virtual environment for project
- Install all dependencies with follow:

``
    (venv)$ pip install requirements.txt
``

## Migrate project
First we can create table in order to migrating project.
```shell script
(venv)$ python manage.py makemigrations
```

You must migrate project in order to create Table in your Database:

```shell script
(venv)$ python manage.py migrate
```

## Run project
```shell script
(venv) $ python manage.py runserver
```

## Descriptions
The project enough to the features with the shop online such as:
- Product
-  Account (login, forgot password, register)
-  Cart
- Order