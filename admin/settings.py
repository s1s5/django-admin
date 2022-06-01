"""
Django settings for admin project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import environ
import yaml

env = environ.Env(
    LANGUAGE_CODE=(str, "ja"),
    TIME_ZONE=(str, "Asia/Tokyo"),
    DATABASE_URL=(str, "sqlite://:memory:"),
    APPS=(str, ""),
    PRIMARY_COLOR=(str, "#79aec8"),
    SECONDARY_COLOR=(str, "#417690"),
    FAVICON_URL=(str, ""),
    ADMIN_INDEX_TITLE=(str, ""),
    ADMIN_SITE_TITLE=(str, ""),
    ADMIN_SITE_HEADER=(str, ""),
    ADMIN_TITLE_PREFIX=(str, ""),
    SECRET_KEY=(str, "django-insecure-xf+7^7slw%(*n@)-9=gx8rjhi50=brt00b9l4%s!k=100c3)rp"),
    SESSION_COOKIE_NAME=(str, "django-admin-sessionid"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "admin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "admin/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "admin.context_processors.export_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "admin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.db_url(),
}
DATABASE_ROUTERS = ["admin.dbrouters.AutoRouter"]


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = env("LANGUAGE_CODE")

TIME_ZONE = env("TIME_ZONE")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

################################################################################

db_set = set()
for app_dict in yaml.safe_load(env("APPS")) or []:
    class_name = app_dict["name"].replace(".", "")
    class_name = class_name[0].upper() + class_name[1:]
    INSTALLED_APPS.append(f"admin.apps.{class_name}")

    db_set.add(app_dict["db"])

for db_name in db_set:
    DATABASES[db_name] = env.db_url(f"{db_name.upper()}_DATABASE_URL", default="sqlite://:memory:")

PRIMARY_COLOR = env("PRIMARY_COLOR")
SECONDARY_COLOR = env("SECONDARY_COLOR")
FAVICON_URL = env("FAVICON_URL")

ADMIN_INDEX_TITLE = env("ADMIN_INDEX_TITLE")
ADMIN_SITE_TITLE = env("ADMIN_SITE_TITLE")
ADMIN_SITE_HEADER = env("ADMIN_SITE_HEADER")
ADMIN_TITLE_PREFIX = env("ADMIN_TITLE_PREFIX")

SESSION_COOKIE_NAME = env("SESSION_COOKIE_NAME")
CSRF_COOKIE_NAME = env("SESSION_COOKIE_NAME") + "-csrftoken"
