import os

class Config:
    SECRET_KEY = 'you-will-never-guess'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass 

config_by_name = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig
}
