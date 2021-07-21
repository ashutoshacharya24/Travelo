# Steps to install and run the server

## Project Setup

### Step 1

Creating virtual environment and activating [Windows]

```
python -m venv venv
venv/Scripts/activate.bat
```

### Step 2

Installing all the dependencies.

```
pip install -r requirements.txt
```

### Step 3

Creating superuser

```
python manage.py createsuperuser
```

### Step 4

Starting the server

```
python manage.py runserver
```

Now your API base url is [localhost:8000](http://localhost:8000/)

## Some API Resource

### Swagger UI [localhost:8000/docs/](http://localhost:8000/docs/)

### To create API Schema

Run

```
python manage.py generateschema --file openapi-schema.yml
```
