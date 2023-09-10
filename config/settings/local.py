from .base import * 
from .base import env

DEBUG = True

# SECRET_KEY = 'django-insecure-qsoved**al6pc8tj=fyt45+c_-b)d_mhoodngiq+%v2u35vby)'
SECRET_KEY = env("DJANGO_SECRET_KEY", default="None")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]