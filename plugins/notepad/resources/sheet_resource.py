from config import Resource
from .. import Sheet, SheetSchema


class SheetResource(Resource):
    schema = SheetSchema()

    def get(self):
        result = self.schema.dump(Sheet.query.all(), many=True)

        return result

    def get_sheet(self, sheet_id):
        result = self.schema.dump(Sheet.query.get(sheet_id))

        return result
