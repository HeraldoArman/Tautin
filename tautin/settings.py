"""
Django settings for tautin project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from typing import Final
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR.joinpath('tautin_app/templates/tautin_app')
STATIC_DIR = BASE_DIR.joinpath('tautin_app/static')


# Get enviroment variable
load_dotenv()
KEY: Final[str] = os.getenv('KEY')
POSTGRES_DATABASE: Final[str] = os.getenv('POSTGRES_DATABASE')
POSTGRES_URL: Final[str] = os.getenv('POSTGRES_URL')
POSTGRES_USER: Final[str] = os.getenv('POSTGRES_USER')
POSTGRES_HOST: Final[str] = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD: Final[str] = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT : Final[str] = os.getenv('POSTGRES_PORT')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'qr_code',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    'tautin_app',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google' : {
        'SCOPE' : [
            'profile',
            'email',
        ],
        'AUTH_PARAMS' : {
            'access_type' : 'online'
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

SOCIALACCOUNT_LOGIN_ON_GET=True
ACCOUNT_EMAIL_VERIFICATION = "none"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'tautin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tautin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': POSTGRES_DATABASE,
#         'USER': POSTGRES_USER,
#         'PASSWORD': POSTGRES_PASSWORD,
#         'HOST': POSTGRES_HOST,
#         'PORT': POSTGRES_PORT,
#         # 'OPTIONS': {
#         #     'sslmode': 'require',
#         # },
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(default=POSTGRES_URL, conn_max_age=600),
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DATABASE,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': '5432',
        'OPTIONS' : {
            'sslmode' : 'require',
            # 'options': 'ep-billowing-waterfall-a1pr41uf',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')

STATICFILES_DIRS = [
    STATIC_DIR,
]

LOGIN_REDIRECT_URL = '/dashboard/'
REGISTER_REDIRECT_URL = '/dashboard/'

LOGOUT_REDIRECT_URL = '/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  
    'allauth.account.auth_backends.AuthenticationBackend',  
)

