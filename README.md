# book_library
books library management API

#The project can be started with two settings from the deploy branch:
1. python manage.py runserver --settings=library_management.settings
   you run development settings sqlite+celery+radis
2. python manage.py runserver --settings=library_management.conf_prod
   you run deploy settings mysql+celery+radis 
