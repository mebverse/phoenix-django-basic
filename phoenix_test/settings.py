import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "core",
]


MIDDLEWARE = []


ROOT_URLCONF = "phoenix_test.urls"

WSGI_APPLICATION = "phoenix_test.wsgi.application"


DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=60,
    )
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
