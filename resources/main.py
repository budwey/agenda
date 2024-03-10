from ..config import Resource
from ..models import SheetModel
from ..schemas import SheetSchema


# Sheet Resources
class Sheet(Resource):
    @staticmethod
    def get():
        sheets = SheetModel.query.all()
        result = SheetSchema(many=True).dump(sheets)

        return result
