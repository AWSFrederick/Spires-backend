# Spires-backend

### Local Dev

Setup /etc/hosts for database.rds.mapfrederick.city to 127.0.0.1

With Docker installed, run:
> docker run -d -e POSTGRES_USER=mapfrederick -e POSTGRES_PASSWORD=mapfrederick -p 5432:5432 postgres

> python manage.py migrate

> python manage.py createcachetable

> python manage.py runserver


### Production setup

> git clone https://github.com/AWSFrederick/Spires-backend.git app
> cd app
> virtualenv env
> source ./env/bin/activate
> pip install -r requirements.txt
> python manage.py migrate
> gunicorn spires.wsgi:application -b 0.0.0.0:5000
