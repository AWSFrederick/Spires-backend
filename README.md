# Spires-backend

> git clone https://github.com/AWSFrederick/Spires-backend.git app
> cd app
> virtualenv env
> source ./env/bin/activate
> pip install -r requirements.txt
> python manage.py migrate
> gunicorn spires.wsgi:application -b 0.0.0.0:5000
