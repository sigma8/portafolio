from instance import config

class Config(object):
    DEBUG = False # Turns on debugging features in Flask
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:4682@localhost:5432/portafolio'

class TestingConfig(Config):
    TESTING = True
