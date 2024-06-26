"""
Django settings for pgsystem project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ # type: ignore


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# DEBUG should be set to False in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'auth_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    
    'projects',
    'wood_delivery',
    'vendor',
    'wood_type',
    'event',
    'certificate',
    'language_switcher'
    
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'auth_app.middleware.UserActivityMiddleware',
]

ROOT_URLCONF = 'pgsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'pgsystem.wsgi.application'

# Set session timeout to 15 minutes (900 seconds)
SESSION_COOKIE_AGE = 900
SESSION_SAVE_EVERY_REQUEST = True

LOGOUT_REDIRECT_URL = '/'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': env('ENGINE'),
#             'NAME': env('NAME'),
#             'USER': env('USER'),
#             'PASSWORD': env('PASSWORD'),
#             'HOST': env('HOST'),
#             'PORT': env('PORT'),
#         }
#     }
    

# Password validation settings
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

# Internationalization settings
LANGUAGES = [
    ('en', 'English'),
    ('ja', 'Japanese'),
]

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True

# Static files settings
STATIC_URL = env('STATIC_URL')
STATIC_ROOT = env('STATIC_ROOT')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files settings
MEDIA_URL = env('MEDIA_URL')
MEDIA_ROOT = env('MEDIA_ROOT')

#Email settings

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS') == 'True'
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
    SERVER_EMAIL = env('SERVER_EMAIL')



# Login settings
LOGIN_REDIRECT_URL = 'auth_app:welcome'
LOGIN_URL = 'auth_app:login_user'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
