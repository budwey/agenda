from api import schema
from api.plugins.sheets import Sheet


class SheetSchema(schema.SQLAlchemyAutoSchema):
    class Meta:
        model = Sheet
