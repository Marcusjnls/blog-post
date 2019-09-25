import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Test configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jean-louis:password@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
