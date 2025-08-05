from .base import *

# https://docs.djangoproject.com/en/dev/ref/settings/
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])
