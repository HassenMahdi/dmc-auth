import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    MONGO_URI = "mongodb://dcm-consmos:pUQRAZMYnTiYikWTxjcq7zQch27litMHCSJnHOu9XCssYxBqVRWmMpd8sSnd0G7w66dQ7GMS4UK8iAvOsoBGtw==@dcm-consmos.mongo.cosmos.azure.com:10255/dcm?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dcm-consmos@"

    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'adm.dcm@outlook.com'
    MAIL_PASSWORD = 'DCMPASS.2020'
    
    PORT = os.getenv('PORT', 5000)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.getenv('MONGO_URI')

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
