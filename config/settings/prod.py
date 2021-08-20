from .base import *
import os

ALLOWED_HOSTS = ['166.104.110.57']
# STATIC_ROOT = BASE_DIR / 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

DEBUG = False
