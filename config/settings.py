from pathlib import Path
import dj_database_url
import os

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security and debugging settings
SECRET_KEY = "django-insecure-d22tmij=75e!gp6sb5v!a2xgkbb()t3m&r#8#+j@rfd_kbz3e("
DEBUG = True  # Set to False in production for security

# Allowed hosts for the Django application
ALLOWED_HOSTS = ["127.0.0.1", "django-shop-nls2.onrender.com"]  # Local and Render hosts

# Application definitions
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shop",  # Custom shop application
    "django.contrib.sites",  # Required for allauth
    # Allauth apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # Providers
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
]

# Middleware configurations
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static file serving
    'allauth.account.middleware.AccountMiddleware',
]

# URL configuration module
ROOT_URLCONF = "config.urls"

# Template configurations
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application definition
WSGI_APPLICATION = "config.wsgi.application"

# Database settings (SQLite for development & render for production)
if os.environ.get("RENDER"):
    # On Render → use Postgres from DATABASE_URL
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    # Local dev → use SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files settings (optional uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth
)

SITE_ID = 2

## 👇 After successful login, go here
LOGIN_REDIRECT_URL = '/'  

# 👇 After logout, go to your custom login page
LOGOUT_REDIRECT_URL = '/login/'  

# 👇 Makes Django's @login_required use your route
LOGIN_URL = '/login/'

SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "optional"
SOCIALACCOUNT_EMAIL_REQUIRED = True
