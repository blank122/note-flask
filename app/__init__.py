from flask import Flask
from .extensions import db, jwt
from .config import Config
from .routes.auth_routes import auth_bp
from .routes.note_routes import note_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(note_bp, url_prefix='/api/notes')

    return app
