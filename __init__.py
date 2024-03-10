from flask import Flask
from .config import Config
from .routes import api as Api
from .models import db as Db
from .schemas import ma as Schema


def core():
    # Initializing app
    app = Flask(__name__)
    # Setup Config
    Config.setup(app)
    # Setup Database
    Db.setup(app)
    # Setup API
    Api.setup(app)
    # Setup Schema
    Schema.setup(app)

    return app
