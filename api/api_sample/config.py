import os


class DevelopmentConfig:

    #Flask
    DEBUG = True

    #SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/api_sample?charset=utf8".format(**{
        'user' : os.getenv('DB_USER','root'),
        'password' : os.getenv('DB_PASSWORD', 'mwmwmw555'),
        'host' : os.getenv('DB_PASSWORD', ''),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig