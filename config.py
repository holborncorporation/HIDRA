import os
from datetime import timedelta


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    PERMANENT_SESSION_LIFETIME =  timedelta(minutes=5)