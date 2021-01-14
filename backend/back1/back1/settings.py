"""
------ DEVELOPMENT -------

Django settings for klaverjas project.

Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

"""

import os
from datetime import timedelta 
from django.core.exceptions import ImproperlyConfigured

# Handling Key Import Errors for loading environment variables
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Get the environent: development or production
ENV = get_env_variable('ENV')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# @ole: extended user model
AUTH_USER_MODEL = 'my_auth.User'

#####################################################################################
#Default settings when no production or development is set as env
DEBUG = False
SECRET_KEY = "testkey"
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MIN_LOG_LEVEL = 'INFO'

#####################################################################################
# load the settings that are specific for development.
# use postgres also in development
if ENV == 'development':
    DEBUG = True
    SECRET_KEY = get_env_variable('SECRET_KEY')
    # ALLOWED_HOSTS = ['localhost','192.168.2.80']
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.2.80','daphne']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_env_variable('DB_NAME'),
            'USER': get_env_variable('DB_USER'),
            'PASSWORD': get_env_variable('DB_PASSWORD'),
            'HOST': get_env_variable('DB_HOST'),
            'PORT': get_env_variable('DB_PORT'),
        }
    }
    MIN_LOG_LEVEL = 'DEBUG'

    # @ole: to support CORS
    CORS_ORIGIN_ALLOW_ALL = True

#####################################################################################
# load the settings that are specific for production.
if ENV == 'production':
    DEBUG = False
    SECRET_KEY = get_env_variable('SECRET_KEY')
    ALLOWED_HOSTS = ['localhost', '127.0.0.1','daphne']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_env_variable('DB_NAME'),
            'USER': get_env_variable('DB_USER'),
            'PASSWORD': get_env_variable('DB_PASSWORD'),
            'HOST': get_env_variable('DB_HOST'),
            'PORT': get_env_variable('DB_PORT'),
        }
    }
    MIN_LOG_LEVEL = 'INFO'

    # @ole: to support CORS
    # CORS_ALLOWED_ORIGINS = [
    #     "https://klaverjasfun.nl",
    #     "http://localhost:80"
    # ]
    CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_auth.apps.My_authConfig',       #@ole: To support self created authentication functionality
    'django_extensions',				#@ole: To support Django extensions
    'django_filters',                   #@ole: too support filtering
    'corsheaders',						#@ole: To support cors headers
    'rest_framework',					#@ole: To support rest framework
    'computed_property',				#@ole: To support computed porperties in models
    'klaverjas',                        #@ole: contains the klaverjas data and views
    'channels',                         #@ole: to support Django channels
    'appwebsocket',                     #@ole: the app to handle the channel communications
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',					# @ole: To support CORS for development
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back1.urls'

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

WSGI_APPLICATION = 'back1.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'     #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#######################################################################################
########### Additional settings #######################################################


# @ole: rest-framework settings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
    	'my_auth.authentication.JWTAuthenticationBlacklist',  				#@ Changed to include blacklist
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],    
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',               # Only allow people to use views when authenticated, default is allowAny
    ]
}

# @ole
# Settings for simple_jwt:  https://github.com/davesque/django-rest-framework-simplejwt/blob/master/README.rst
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# @ole: Add the ASGI application for channels 
ASGI_APPLICATION = 'back1.routing.application'

# @oleand add redis server address/port
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [('127.0.0.1', 6379)],
            "hosts": [(get_env_variable('REDIS_HOST'), 6379)],
        },
    },
}

# @ole Mail
## Mail settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_USE_TLS = get_env_variable('EMAIL_USE_TLS')
EMAIL_PORT = get_env_variable('EMAIL_PORT')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')