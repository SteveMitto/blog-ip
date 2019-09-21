from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options
app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = ('auth.login')
login_manager.session_protection = "strong"

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth)
    from .blog import blog
    app.register_blueprint(blog)
    db.init_app(app)
    login_manager.init_app(app)
    return app
