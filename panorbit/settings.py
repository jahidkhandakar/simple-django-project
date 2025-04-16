import os

# ────────────────
# Basic Setup
# ────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3xb%+*2uex+%1&$@=*+(@^atnm!#tz-n&i5qn$o46jnp&u*2l^'
DEBUG = True

ALLOWED_HOSTS = ["c9ae666b.ngrok.io", "localhost"]

# ────────────────
# Installed Apps
# ────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'haystack',
    'phonenumber_field',

    # Local apps
    'world',
]

# ────────────────
# Middleware
# ────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ────────────────
# URL Configuration
# ────────────────
ROOT_URLCONF = 'panorbit.urls'

# ────────────────
# Templates
# ────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# ────────────────
# WSGI Application
# ────────────────
WSGI_APPLICATION = 'panorbit.wsgi.application'

# ────────────────
# Database
# ────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME", "world"),
        'USER': os.getenv("DB_USER", "root"),
        'PASSWORD': os.getenv("DB_PASSWORD", "root"),
        'HOST': os.getenv("DB_HOST", "db"),  # Use service name for Docker
        'PORT': os.getenv("DB_PORT", "3306"),
    }
}

# ────────────────
# Password Validators
# ────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ────────────────
# Internationalization
# ────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ────────────────
# Static Files
# ────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ────────────────
# Authentication
# ────────────────
AUTH_USER_MODEL = 'world.User'
LOGIN_URL = 'signup'

# ────────────────
# Email Configuration
# ────────────────
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_email@gmail.com'         # ✅ Replace with your Gmail
EMAIL_HOST_PASSWORD = 'your_app_password_here'   # ✅ Replace with your app password
EMAIL_PORT = 587

# For local testing (optional)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ────────────────
# Haystack Search
# ────────────────
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
