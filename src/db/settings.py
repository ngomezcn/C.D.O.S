import os
from decouple import config

DEBUG = False

# Database
if DEBUG:
    SERVER = 'localhost'
    DATABASE = 'postgres'
    USERNAME = 'postgres'
    PASSWORD = '1234'
    PORT = '5432'
else:
    SERVER = 'taplock.app'
    DATABASE = 'cdos'
    USERNAME = 'cdos'
    PASSWORD = config('PROD_DB_PASSWORD')
    PORT = '5432'

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}'
