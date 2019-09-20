import os
from dotenv import load_dotenv
load_dotenv()
class Config(object):
    """Class for the parent Config."""

class ProdConfig(Config):
    """Class for the parent Config."""

class DevConfig(object):
    """Class for the parent Config."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

config_options={
'production':ProdConfig,
'development':DevConfig
}
