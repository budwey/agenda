from flask import Flask
from core import db, api
from config import Config

# Plugin imports
from plugins import (
    notepad_routes as notepad
)

# Available plugins
plugins = [
    notepad
]


def core():
    # Setup app
    app = Flask(__name__)
    # Setup config
    Config.setup(app)
    # Setup plugins
    Config.register_plugins(app, plugins)
    # Setup Database
    db.setup(app)
    # Setup API
    api.setup(app)

    print(app.url_map)

    return app
