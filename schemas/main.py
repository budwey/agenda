from ..config import Schema
from ..models import SheetModel

ma = Schema()


class SheetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SheetModel
        load_instance = True
