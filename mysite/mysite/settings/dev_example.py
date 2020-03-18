"""
Add dev.py to .gitignore as it contains secret info! This is just a demo of how it should look.
"""

from .base import *
import os
import environ


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'insert_secret_key_here'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['insert', 'allowed', 'hosts'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insert_db_name',
        'USER': 'insert_db_user',
        'PASSWORD': 'insert_db_password',
        'HOST': 'localhost',
        'PORT': 'insert_db_port',
    }
}




try:
    from .local import *
except ImportError:
    pass



# uncomment before deployment:

SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

SECURE_SSL_REDIRECT = False

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

