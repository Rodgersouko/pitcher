import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    '''
    General configuration parent class
    '''
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Access@localhost/pitcher'
    DEBUG = True


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    #MAIL_USERNAME = os.environ.get("moringa")
    MAIL_PASSWORD = os.environ.get("Access")
    SENDER_EMAIL = 'gabrielaouko@gmail.com'
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL')


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    
    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig
}