from ..config import Api
from ..resources import Sheet

api = Api()

# Sheet Routes
api.add_resource(Sheet, '/')
