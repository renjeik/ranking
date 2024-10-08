"""
Django settings for RankingPortalCore project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from distutils.util import strtobool

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ic6t#7_b3xe=5r41cxjs%gvh4$l(r4nw7%i3p&!j&=&6!84!-n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DJANGO_LOG_LEVEL = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = [
    "127.0.0.1",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        }
    },
}

# Application definition

INSTALLED_APPS = [
    "debug_toolbar",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_swagger",
    "rest_framework",
    "drf_yasg",
    "RankingPortalCore",
    "UserInterface",
    "UserManagement",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # TODO: Do not know if removing CSRF middleware is secure or not
    #'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

ROOT_URLCONF = "RankingPortalCore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "UserInterface/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "staticfiles": "django.templatetags.static",
            },
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

WSGI_APPLICATION = "RankingPortalCore.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {}

if strtobool(os.environ.get("MYSQL_ACTIVE", "false")):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",  # (pip install mysqlclient)
            "NAME": os.environ.get("MYSQL_DATABASE", "mysql-db"),
            "USER": os.environ.get("MYSQL_USER", "mysql-user"),
            "PASSWORD": os.environ.get("MYSQL_PASSWORD", "mysql-password"),
            "HOST": os.environ.get("MYSQL_DATABASE_HOST", "mysql-db"),
            "PORT": os.environ.get("MYSQL_DATABASE_PORT", 3306),
            "TEST": {
                "NAME": "mysql-db-test"
            }
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "TEST": {
                "NAME": "sqlite-db-test"
            }
        }
    }

SESSION_COOKIE_NAME = "sessionid"

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/UserInterface/static/"
STATICFILES_DIRS = [BASE_DIR / "UserInterface/static/"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Module configuration
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html

# All values are default values
DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    "RESULTS_CACHE_SIZE": 25,
    "SHOW_COLLAPSED": True,
    # Panel options
    "SQL_WARNING_THRESHOLD": 500,  # milliseconds
}
