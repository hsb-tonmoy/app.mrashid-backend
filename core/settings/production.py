import os
from .development import *
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEBUG = False
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', False)

ALLOWED_HOSTS = ['api.mrashid.net', '127.0.0.1', '0.0.0.0',
                 'localhost', 'app-mrashid.herokuapp.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),

    integrations=[DjangoIntegration()],

    traces_sample_rate=1.0,

    send_default_pii=True
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
