from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
app = Flask(__name__)
db = SQLAlchemy()

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth)
    db.init_app(app)
    return app
