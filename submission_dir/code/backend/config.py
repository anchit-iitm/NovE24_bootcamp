# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''

class LocalDev(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = "shhh.... its secret"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'donot-reply@a.com'
    
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 2
    CACHE_DEFAULT_TIMEOUT = 60


class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://server.address/db.sqlite3'

class celeryConfig():
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/1'
    timezone = 'Asia/Kolkata'