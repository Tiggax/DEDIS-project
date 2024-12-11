from .default import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": cfg["DB_NAME"],
        "USER": cfg["DB_USER"],
        "PASSWORD": cfg["DB_PASSWORD"],
        "HOST": cfg["DB_HOST"],
        "PORT": cfg["DB_PORT"],
    }
}
