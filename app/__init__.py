from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['FILES_DIR'] = os.environ.get('FILES_DIR', '/files')

    from .routes import bp
    app.register_blueprint(bp)

    return app
