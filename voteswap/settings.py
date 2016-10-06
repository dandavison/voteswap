"""
Django settings for voteswap project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from voteswap.cloud_settings import CloudSettings

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CloudSettings.get('secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CloudSettings.get('debug') == "True"

SOCIAL_AUTH_FACEBOOK_KEY = CloudSettings.get('facebook_key')
SOCIAL_AUTH_FACEBOOK_SECRET = CloudSettings.get('facebook_secret')
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    "public_profile",
    "email",
    "user_friends",
]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email,friends',
}

# Sendgrid email
SENDGRID_API_KEY = CloudSettings.get('sendgrid_api_key')
if CloudSettings.is_local:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'voteswap.mail.backends.sendgrid.SendGridBackend'

LOGIN_REDIRECT_URL = '/'

ALLOWED_HOSTS = [
    'voteswap.us',
    '2016-10-02-dot-voteswap-142902.appspot.com',
    '2016-10-03-dot-voteswap-142902.appspot.com',
    '2016-10-05-dot-voteswap-142902.appspot.com',
    '2016-10-05-1-dot-voteswap-142902.appspot.com',
]

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
APPS_DIR = os.path.join(ROOT_DIR, 'voteswap')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'voteswap',
    'polling',
    'users',
    'bootstrap3',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]

# See http://psa.matiasaguirre.net/docs/configuration/django.html#django-admin
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

AUTHENTICATION_BACKENDS = [
    'social.backends.facebook.Facebook2OAuth2',  # FaceBook OAuth2 Graph2.0
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'voteswap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(os.path.join(APPS_DIR, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'voteswap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': CloudSettings.get('database_engine'),
            'HOST': CloudSettings.get('database_host'),
            'NAME': CloudSettings.get('database_name'),
            'USER': CloudSettings.get('database_user'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': CloudSettings.get('database_engine'),
            'HOST': CloudSettings.get('database_host'),
            'PORT': CloudSettings.get('database_port'),
            'NAME': CloudSettings.get('database_name'),
            'USER': CloudSettings.get('database_user'),
            'PASSWORD': CloudSettings.get('database_password'),
        }
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s][%(levelname)s::%(module)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': CloudSettings.get('log_level').upper(),
            'propagate': True,
        },
        'voteswap': {
            'handlers': ['console'],
            'level': CloudSettings.get('log_level').upper(),
            'propagate': True,
        },
        'users': {
            'handlers': ['console'],
            'level': CloudSettings.get('log_level').upper(),
            'propagate': True,
        },
        'polling': {
            'handlers': ['console'],
            'level': CloudSettings.get('log_level').upper(),
            'propagate': True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # NOQA
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'vendor_static'),
    os.path.join(BASE_DIR, 'voteswap', 'static')
]

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
