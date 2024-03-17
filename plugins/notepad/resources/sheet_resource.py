from config import Resource
from .. import Sheet, SheetSchema


class SheetResource(Resource):
    schema = SheetSchema()

    def get(self, id=None):
        if id:
            result = self.schema.dump(Sheet.query.get(id))
        else:
            result = self.schema.dump(Sheet.query.all(), many=True)

        return result
