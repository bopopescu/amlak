"""
Django settings for amlak2 project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os




#import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from django.contrib.gis.gdal import libgdal
if os.name == 'nt':
    import platform
    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# os.environ['PATH'] = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo') + ';' + os.environ['PATH']

# os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']

# GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, 'venv\Lib\site-packages\osgeo\gdal300.dll') 

# SITE_PATH = os.path.abspath(os.path.dirname(__file__))
# MAP_WIDGETS_PATH = os.path.normpath(os.path.join(SITE_PATH, '..', '..', '..'))
# if MAP_WIDGETS_PATH not in sys.path:
#     sys.path.insert(0, MAP_WIDGETS_PATH)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cu(8x4*#_3*_0ll%#gw!fd)^@u%f_@rq94z$av0*h(o7-(e2i-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'crispy_forms',
    'django_jalali',
    'bootstrap4',
    'django_filters',
    'cleanup',
    'ckeditor',
    #'ckeditor_uploader',
    'rest_framework',
    'report_builder',
    'csvimport.app.CSVImportConf',  # use AppConfig for django >=1.7 csvimport >=2.2
]


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,

    'DEFAULT_AUTHENTICATION_CLASSES': (
       
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

    
    ]
}

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'map.zoom': 15,

    'search.provider': 'google',
    'search.suffix': '',

    # # Google
    # 'provider.google.api': '//maps.google.com/maps/api/js?sensor=false',
    # 'provider.google.api_key': '<INSERT GOOGLE API KEY>',
    # 'provider.google.api_libraries': '',
    # 'provider.google.map.type': 'ROADMAP',
    #
    # # Mapbox
    # 'provider.mapbox.access_token': '',
    # 'provider.mapbox.max_zoom': 18,
    # 'provider.mapbox.id': 'mapbox.streets',

    # OpenStreetMap
    'provider.openstreetmap.max_zoom': 16,

    # # misc
    # 'resources.root_path': LOCATION_FIELD_PATH,
    # 'resources.media': {
    #     'js': (
    #         LOCATION_FIELD_PATH + '/js/form.js',
    #     ),
    # },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amlak2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'amlak2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#import dj_database_url

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME':'Amlak2' ,
        'USER':'root',
        'PASSWORD':'33752788',
        'HOST':'localhost',
        'PORT':'3306',
    }
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'
import locale
locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'index'
# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
# CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media')



