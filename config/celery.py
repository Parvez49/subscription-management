import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

app = Celery('subscription-management')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Configure Celery Beat schedule for the task
app.conf.beat_schedule = {
    "fetch-exchange-rate": {
        "task": "project_apps.subscriptions.tasks.fetch_usd_to_bdt_rate",
        "schedule": timedelta(minutes=60),  # 1 hour
    },
}
