from instance import config

class Config(object):
    DEBUG = False # Turns on debugging features in Flask
    TESTING = False
    

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
