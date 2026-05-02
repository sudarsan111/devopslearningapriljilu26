from flask import Flask
from .routes import tasks_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)
    return app
