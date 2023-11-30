import os

from .settings import *

import pymysql
pymysql.install_as_MySQLdb()

ALLOWED_HOSTS = ['*']

# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
SECRET_KEY = '#3%h*qnnte66)u%w+@i2k1+u0$n(=1bp)96(nv(@$xz-5*1e^x'
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_library',
        'USER': os.getenv("MYSQL_USERNAME"),
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST': 'db',
        'PORT': '3306',
    }
}

# del STATICFILES_DIRS
STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
   ]
STATIC_ROOT = '/app/staticfiles'

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'