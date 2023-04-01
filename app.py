from flask import Flask
from flask_cors import CORS

from api.models import db
from api.config import Config
from api.api import api,Version

def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    register_extension(app)
    return app

def register_extension(app):
    api.init_app(app)
    db.init_app(app)

app = create_app(Config)


if __name__ == '__main__':
    app = create_app(Config)
    app.run(host='0.0.0.0',port=5000)