from flask import Blueprint
from api.config import Api
from api.plugins.sheets import SheetResource

plugin = Blueprint('sheets', __name__)
sheets = Api(plugin)

SheetPlugin = {
    'prefix': '/sheet',
    'resources': plugin
}

# Sheet routes
sheets.add_resource(SheetResource, '/<sheet_id>')
