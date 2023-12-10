"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["toolmanager-env.eba-x9pzmsw3.eu-west-2.elasticbeanstalk.com", "127.0.0.1", "18.130.19.180"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "machines",
    "users",
    "tools_assembly",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_extensions",
    "fontawesomefree",
    "notifications",
    "holders",
    "tools",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "base.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "machines.context_processors.all_machines",
                "machines.context_processors.user_notifications",
            ],
        },
    },
]

WSGI_APPLICATION = "base.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db_podzial_apek.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': 'db',
#         'PORT': env("DB_PORT"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ("pl", _("Polish")),
    ("en", _("English")),
]

LANGUAGE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
    os.path.join(BASE_DIR, "tools/locale"),
    os.path.join(BASE_DIR, "holders/locale"),
    os.path.join(BASE_DIR, "tools_assembly/locale"),
    os.path.join(BASE_DIR, "machines/locale"),
    os.path.join(BASE_DIR, "notifications/locale"),
]


TIME_ZONE = "UTC"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "login"

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s.%(lineno)d] %(message)s",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "warning.log",
            "formatter": "standard",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "filters": [],
        },
    },
    "loggers": {
        "django": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "django.request": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "django.db.backends": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "django.template": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "machines": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "notifications": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "tools_assembly": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },
        "users": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },
    },
    # 'root': {
    #     'level': 'INFO',
    #     'handlers': ['console', 'file'],
    # },
}
