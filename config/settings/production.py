from .staging import *

# https://django-storages.readthedocs.io/en/latest/#installation
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
INSTALLED_APPS += ['storages']
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': f'max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate',
}
AWS_S3_MAX_MEMORY_SIZE = env.int('AWS_S3_MAX_MEMORY_SIZE', default=100_000_000),  # 100MB
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', default=None)
AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', default=None)
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# https://docs.djangoproject.com/en/dev/ref/settings/#storages
STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {
            'location': 'media',
            'file_overwrite': False,
            'querystring_auth': True,
        },
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3.S3Storage',
        'OPTIONS': {
            'location': 'static',
            'default_acl': 'public-read',
        },
    },
}

MEDIA_URL = f'https://{aws_s3_domain}/media/'
STATIC_URL = f'https://{aws_s3_domain}/static/'
