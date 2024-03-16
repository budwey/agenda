from plugins.notepad import SheetResource
from plugins.notepad.routes import api

# Sheet routes
api.add_resource(SheetResource, '/<sheet_id>')
