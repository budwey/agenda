from config import Resource
from plugins.notepad import Sheet, SheetSchema


class SheetResource(Resource):
    @classmethod
    def get(cls, sheet_id):
        sheet = Sheet.query.get(sheet_id)
        if sheet is None:
            return None

        schema = SheetSchema()
        result = schema.dump(sheet)

        return result

