# runinkarun config

Activar entorno virtual:

    1)En Mac: source env/bin/activate
    2)En Windows: env/Scripts/activate
    3)En Git Bash (Windows): source Scripts/activate

Run app:

    1)En Mac: python3 manage.py runserver
    2)En Windows: python manage.py runserver

Some configurations:

    1) django-admin.py startproject nombre
    2) django-admin.py startapp nombre
    3) django-admin.py createsuperuser
    4) python manage.py makemigrations
    5) python manage.py migrate

Instalando paquetes:

    1) pip install djangorestframework
    2) pip install mysqclient

The app is deployed in Heroku PaaS services:

Url: http://runinkarun.herokuapp.com/

Note:
    -To rename app from the CLI use command: heroku apps:rename newname --app oldname

App is using as database Heroku Postgres Service (PostgreSQL)
