afrom .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ('ALLOWED_HOSTS').split.(',')

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': 'rosamund',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


