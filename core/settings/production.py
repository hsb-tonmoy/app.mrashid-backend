from .development import *
import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DEBUG = False
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['api.mrashid.net', '127.0.0.1', '0.0.0.0',
                 'localhost', 'app-mrashid.herokuapp.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

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
