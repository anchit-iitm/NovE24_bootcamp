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


class Production(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://server.address/db.sqlite3'