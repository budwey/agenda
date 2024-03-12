import os
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api as ApiRestful, Resource as ResourceRestful
from constants import flask_env, envs, env_params, messages


class Config:
    app_root = os.path.join(os.path.dirname(__file__))
    env = os.getenv(flask_env) or envs.prod.name

    @classmethod
    def get(cls):
        env = os.path.join(cls.app_root, envs[cls.env].get('path'))

        load_dotenv(env)
        return os.environ

    @classmethod
    def setup(cls, app):
        config = cls.get()
        for key, value in config.items():
            if key in env_params.values():
                app.config[key] = value

    @classmethod
    def register_plugins(cls, app, plugins):
        for plugin in plugins:
            resource = plugin.get('resources')
            prefix = plugin.get('prefix')
            app.register_blueprint(resource, url_prefix=prefix)


class Database(SQLAlchemy):
    def __init__(self):
        super().__init__()

    def setup(self, app):
        self.init_app(app)
        with app.app_context():
            self.create_all()
            print(messages.get('db').get('success'))


class Api(ApiRestful):
    def __init__(self, app=None):
        super().__init__(app)

    def setup(self, app):
        self.init_app(app)
        print(f"{messages.get('api').get('success')}")


class Resource(ResourceRestful):
    def __init__(self, app=None):
        super().__init__(self, app)


class Schema(Marshmallow):
    def __init__(self):
        super().__init__()

    def setup(self, app):
        self.init_app(app)
        print(messages.get('schemas').get('success'))
