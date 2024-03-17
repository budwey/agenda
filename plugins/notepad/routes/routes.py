from flask import Blueprint
from config import Api
from .sheet_route import sheets_api

plugin = Blueprint('notepad', __name__)
api = Api(plugin)

# Defining API namespaces
api.add_namespace(sheets_api, '/sheets')

# Exporting API
notepad_routes = {
    'prefix': '/notepad',
    'resources': plugin
}
