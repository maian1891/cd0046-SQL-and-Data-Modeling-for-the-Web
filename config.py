import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database
database_url = 'postgresql://postgres:123456@localhost:5433/Fyyur'
SQLALCHEMY_DATABASE_URI = database_url
