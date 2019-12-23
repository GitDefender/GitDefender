import os, json
from datetime import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open(BASE_DIR+'/gitdefender/key.json', 'r')  as key:
    key = json.loads(key.read())
    SECRET_KEY = key['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'app',
    'knox',
    'drf_yasg',
    'corsheaders',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'gitdefender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
        ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

WSGI_APPLICATION = 'gitdefender.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

with open(BASE_DIR+'/gitdefender/key.json', 'r') as key:
    key = json.loads(   key.read())

    DATABASES = {
    'default': {
        'ENGINE': key['DB']['ENGINE'],
        'NAME': key['DB']['NAME'],
        'HOST': key['DB']['HOST'],
        'USER': key['DB']['USER'],
        'PASSWORD': key['DB']['PASSWORD'],
        'PORT': key['DB']['PORT']
    }
}

CORS_ORIGIN_ALLOW_ALL = True

# MUST ONLY DEVELOP MODE
CORS_ALLOW_CREDENTIALS = True

"""
# -production-

CORS_ORIGIN_WHITELIST = [
    'localhost:8000'
]
"""

with open(BASE_DIR+'/gitdefender/key.json', 'r') as key:
    key = json.loads(key.read())

    SWAGGER_SETTINGS = {
        'VALIDATOR_URL': 'http://localhost:8189',
        'USE_SESSION_AUTH': True,
        'SECURITY_DEFINITIONS': {
            'api_key': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            }
        },
        'OAUTH2_CONFIG': {
        'clientId': key['CLIENT_ID'],
        'clientSecret': key['CLIENT_SECRET'],
        'appName':  key['USER_AGENT'],
            },
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'TOKEN_TTL': timedelta(hours=5),
    'TOKEN_LIMIT_PER_USER': 1,
    'AUTO_REFRESH': True,
    
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH=False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
