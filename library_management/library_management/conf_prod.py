import os

from .settings import *

import pymysql
pymysql.install_as_MySQLdb()

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_library',
        'USER': os.getenv("MYSQL_USERNAME"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# del STATICFILES_DIRS
# STATIC_ROOT = BASE_DIR / "static"

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'