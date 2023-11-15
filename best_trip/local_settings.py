from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7-jd8@1_jet24qyiv5f8vnr4ew+)h5^uhg1n)sk_rizfj@wvwr'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'google_trip_db',
        'USER': 'ksgorbunov',
        'PASSWORD': '21Russia!',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_ROOT = Path(BASE_DIR, 'static')
