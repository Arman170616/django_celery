# django_celery/celery.py


import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcelery.settings")

app = Celery("djcelery")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()