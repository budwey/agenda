from flask import jsonify

from api.config import Resource
from api.plugins.sheets import Sheet, SheetSchema


class SheetResource(Resource):
    @classmethod
    def get(cls, sheet_id):
        sheet = Sheet.query.get(sheet_id)
        if sheet is None:
            return None

        schema = SheetSchema()
        result = schema.dump(sheet)

        return 'test'