# Config pyfile for aita
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'dev'
    DATABASE='mongodb://localhost:27017/'

class Production(Config):
    """ Generate production secrete key
    import os
    os.urandom(24)
    """
    # SECRET_KEY = 'production'
    pass

class Development(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True