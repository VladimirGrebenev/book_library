# book_library
books library management API

# The project can be started with two settings from the deploy branch:
1. python manage.py runserver --settings=library_management.settings
   you run development settings sqlite+celery+radis
2. python manage.py runserver --settings=library_management.conf_prod
   you run deploy settings mysql+celery+radis 

# You can quickly fill the database with the following commands:
1. python manage.py fillusers
2. python manage.py fillbooks

# If you want Mysql:
you must dont forget set settings to evn: export DJANGO_SETTINGS_MODULE="library_management.conf_prod",
install Mysql, create DB

# CELERY 'hello_mail':
Now REDIS send mail to file to var/email-messages/
You can change this simple in settins, just set your EMAIL settings and
dont forget to chancge EMAIL_BACKEND

# CORS:
!!! be careful.
now in settings.py
CORS_ALLOWED_ORIGINS = ["http://localhost:3000",]
and in conf_prod.py
ALLOWED_HOSTS = ['*']
more about CORS here https://pypi.org/project/django-cors-headers/

# HOW TO RUN:

## simple run -> 
pull MASTER branch from github, 
pip install requirements.txt,
python manage.py fillusers,
python manage.py fillbooks,
python manage.py runserver

## docker run (DRF+MYSQL+REDIS+GUNICORN+NGINX)->
pull DEPLOY branch from github,
install docker and docker-compouse,
run on terminal: docker compose up --build 
(!!! sorry, but you must know that static_files not working in Nginx)




