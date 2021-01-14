import os

DB_USERNAME_CLK = os.environ.get('DB_USERNAME_CLK')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME_CLK = os.environ.get('DB_NAME_CLK')


class BaseConfig(object):
    DEGUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEGUG = True
    SECRET_KEY = 'thisIsADevKey'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME_CLK}:{DB_PASSWORD}@localhost/{DB_NAME_CLK}'


class ProdConfig(BaseConfig):
    DEGUG = False
