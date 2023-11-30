import os
from django.conf import settings
from celery import Celery

if settings.DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_management.settings")

celery_app = Celery("library_management")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
