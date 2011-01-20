BASE PROJECT
============

### On this project all others are built

This is originally built off of the Pinax account project

When starting a new project:

1. Setup fixtures/initial_data.json
1. Setup local_settings.py
1. Setup PIL, Python, Postgres or SQLite on machine
1. 

    pip install -r requirements/dev.txt
    python manage.py syncdb

5. Do Not create a user

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

