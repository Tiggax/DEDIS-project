# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

from .default import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


LOGGING["level"] = "DEBUG"