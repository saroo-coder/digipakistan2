"""
Django settings for digipakistan project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nzq+oudj96g%-g2sf=_t3^ts_@v)&5hh_a%0(a3xlwl(rtvmw4'

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
    'django.contrib.sites',

    # ****** API ********
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'auth_users.apps.AuthUsersConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    # ****** APPS ********
    'learn.apps.LearnConfig',
    'teacherApp.apps.TeacherAppConfig',
    'Product.apps.ProductConfig',
    'superadmin.apps.SuperadminConfig',
    'adminapp.apps.AdminappConfig',
    'parentApp.apps.ParentappConfig',
    'client.apps.ClientConfig',
    'Student.apps.StudentConfig',
    
    # ****** APPS ********

    



    # ****** API ********
]

# REST_FRAMEWORK = {
#     # 'DEFAULT_AUTHENTICATION_CLASSES': [
#     #     #'auth_users.backends.JWTAuthentication',
#     #     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     #     'rest_framework.authentication.SessionAuthentication',
#     #     'rest_framework.authentication.TokenAuthentication',

#     # ],
#     # # Use Django's standard `django.contrib.auth` permissions,
#     # # or allow read-only access for unauthenticated users.
#     # 'DEFAULT_PERMISSION_CLASSES': [
#     #     'rest_framework.permissions.DjangoModelPermissions',

#     # ],
#     # 'DEFAULT_PARSER_CLASSES': [
#     #     'rest_framework.parsers.JSONParser',
#     # ]
# }

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

AUTH_USER_MODEL = 'auth_users.USER'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

# CORS
    # .........
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # .........

]
# CORS
# .............
CORS_ORIGIN_ALLOW_ALL = True
# .............
CSRF_COOKIE_NAME = 'csrftoken'
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False


ROOT_URLCONF = 'digipakistan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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
# AUTH_USER_MODEL = 'auth_users.USER'
# AUTH_USER_MODEL = 'auth.USER'

WSGI_APPLICATION = 'digipakistan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'teachermodel',
         'USER': 'postgres',
         'PASSWORD': 'root',
         'HOST': 'localhost',
         'PORT': '5432',
    # }

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sarooshtahir22@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'



STATICFILES_DIRS = [os.path.join(BASE_DIR, "myproject", "site_static")]
STATIC_ROOT = os.path.join(BASE_DIR, "digipakistan2", "static")
STATIC_URL = "/static/"
MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = '/rest-auth/login/'
CORS_ORIGIN_ALLOW_ALL = True 