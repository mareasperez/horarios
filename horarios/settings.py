"""
Django settings for horarios project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv
import dj_database_url
import django_heroku 
if os.path.exists(".env"):
    load_dotenv()
    print("loading environment for: " + str(os.environ.get("ENVIRONMENT")))
else:
    print("No .env file found")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ftr-y0576^@me8k6hki_-ri6q8*p5$za0jku7txry0g)2pun2$"

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True if os.environ.get("ENVIRONMENT") == "DEV" else False
print ("DEBUG: " + str(DEBUG))
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:4200",
#     "http://127.0.0.1:4200",
#     "https://localhost:4200",
#     "https://127.0.0.1:4200",
#     "https://localhost:8080",
#     "http://127.0.0.1:8080",
#     "http://localhost:8080"
# ]

# Application definition
THIRD_PARTY_APPS = [
    "channels",
    "corsheaders",
    "rest_framework",
    # 'rest_framework.authtoken',
    "reset_migrations",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "apps.facultades",
    "apps.docentes",
    "apps.aulas",
    "apps.recintos",
    "apps.carreras",
    "apps.grupos",
    "apps.departamento",
    "apps.plan_de_estudio",
    "apps.area",
    "apps.componentes",
    "apps.docente_area",
    "apps.planificacion",
    "apps.docente_horas",
    "apps.horario",
    "apps.websocket",
    "apps.mymid",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "horarios.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "horarios.wsgi.application"
# Channels
ASGI_APPLICATION = "horarios.asgi.application"

# Usar Redis como backend de los canales
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get("REDIS_URL", "redis://localhost:6379")],
        },
    },
}

# Usar canales en memoria para evitar la dependencia a redis
# gasta mas memoria en el servidor local
# CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'horariosdb',
#          'USER': 'usuario',
#          'PASSWORD': 'noquiero',
#          'HOST': 'localhost',
#          'PORT': '5432',
#      }
#  }
DATABASES = {
    # environment variable
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"), conn_max_age=600
    )
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase.db',
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
from datetime import timedelta

# REST_FRAMEWORK = {
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=600),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    #     'ROTATE_REFRESH_TOKENS': False,
    #     'BLACKLIST_AFTER_ROTATION': True,
    #
    #     'ALGORITHM': 'HS256',
    #     'SIGNING_KEY': SECRET_KEY,
    #     'VERIFYING_KEY': None,
    #
    #     'AUTH_HEADER_TYPES': ('Bearer',),
    #     'USER_ID_FIELD': 'id',
    #     'USER_ID_CLAIM': 'user_id',
    #
    #     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    #     'TOKEN_TYPE_CLAIM': 'token_type',
    #
    #     'JTI_CLAIM': 'jti',
    # # no se pa que puta sirve pero la doc esta
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=600),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}
JWT_AUTH = {
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
}
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "es-Es"

TIME_ZONE = "America/Managua"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = "/static/"
# # STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# MEDIA_URL = '/public/'
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
print(STATIC_ROOT)
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/public/"
django_heroku.settings(locals())
