from config import Namespace
from .. import SheetResource

# Sheet API Definition
sheets_api = Namespace('sheets', 'Sheet routes')

# Sheet API Routes
sheets_api.add_resource(
    SheetResource,
    '/<sheet_id>',
    method = 'get_sheet'
)
