# Development settings


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z41)x&_-^wv3-!-&9=!t_i1$yos5js7ymt&i28h^zq#h8n5pc6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ('127.0.0.1')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@lavilotte-rolle.fr'
EMAIL_SUBJECT_PREFIX = '[Photobook]'



ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Lavilotte-Rolle Frederic', 'pro@lavilotte-rolle.fr'),
)
MANAGERS = ADMINS


# Allow CORS for developpment
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    '127.0.0.1:3000'
)
CORS_ALLOW_CREDENTIALS = True



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


