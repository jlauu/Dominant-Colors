import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  UPLOAD_FOLDER = 'static/images/'
  ALLOWED_EXTENSIONS = set(['jpg'])
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
