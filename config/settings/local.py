from .base import *
from .base import env

DEBUG = True

# SECRET_KEY = 'django-insecure-qsoved**al6pc8tj=fyt45+c_-b)d_mhoodngiq+%v2u35vby)'
SECRET_KEY = env("DJANGO_SECRET_KEY", default="None")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "info@devops.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Devops"