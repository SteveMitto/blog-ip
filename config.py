import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    """Class for the parent Config."""
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    """Class for the parent Config."""

class DevConfig(Config):
    """Class for the parent Config."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS =False
config_options={
'production':ProdConfig,
'development':DevConfig
}
