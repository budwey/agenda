from flask import Blueprint
from config import Api

plugin = Blueprint('notepad', __name__)
api = Api(plugin)

notepad_routes = {
    'prefix': '/notepad',
    'resources': plugin
}
