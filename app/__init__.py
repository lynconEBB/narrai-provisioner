from flask import Flask
from app.routes.captive_portal import captive_bp
from app.routes.user import user_bp
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(captive_bp)

    return app