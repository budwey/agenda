import os
from urllib.parse import urlencode, urlparse, parse_qs

from dotenv import load_dotenv
from flask import url_for, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_restx import (
    Api as ApiRest,
    Resource as ResourceRest,
    Namespace as NamespaceRest
)
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
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
    def is_development(cls):
        return cls.env == 'env'

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

    def setup(self, app, dev=False):
        self.init_app(app)
        print(messages.get('db').get('success'))
        if dev:
            with app.app_context():
                self.drop_all()
                self.create_all()


class Api(ApiRest):
    def __init__(self, app=None):
        super().__init__(app)

    def setup(self, app):
        self.init_app(app)
        print(f"{messages.get('api').get('success')}")


class Namespace(NamespaceRest):
    def add_resource(self, resource, *urls, **kwargs):
        return super().add_resource(resource, *urls, **kwargs)


class Resource(ResourceRest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Schema(SQLAlchemyAutoSchema):
    def dump(self, obj, *, many=None, total=0, page=None, limit=None, **kwargs):
        if page is None or limit is None:
            page, limit = self.extract_pagination_from_url()

        data = super().dump(obj, many=many)

        output = {}

        if many is not None:
            embedded_data = []
            for item in data:
                embedded_item = item.copy()
                links = self.get_links(item)
                if links:
                    embedded_item["_links"] = links
                embedded_data.append(embedded_item)
            output["total"] = len(embedded_data)
            output["page"] = page
            output["limit"] = limit
            output["_embedded"] = embedded_data
        else:
            output["page"] = page
            output["limit"] = limit
            output.update(data)
            links = self.get_links(data)
            if links:
                output["_links"] = links

        root_links = self.get_collection_links(page=page, limit=limit)
        if root_links:
            output["_links"] = root_links

        return output

    @staticmethod
    def extract_pagination_from_url():
        parsed_url = urlparse(request.url)
        query_params = parse_qs(parsed_url.query)
        page = int(query_params.get('page', [1])[0])
        limit = int(query_params.get('limit', [20])[0])
        return page, limit

    @staticmethod
    def get_links(obj):
        links = {}
        if obj:
            endpoint = request.endpoint
            url = url_for(endpoint, id=obj['id'], _external=True)
            links["self"] = {"href": url}
        return links

    @staticmethod
    def get_collection_links(page=1, limit=None, **kwargs):
        links = {}
        endpoint = request.endpoint
        url = url_for(endpoint, _external=True)

        url_params = {"page": page, "limit": limit}
        url_params.update(kwargs)

        links["self"] = {"href": url + "?" + urlencode(url_params)}

        return links
