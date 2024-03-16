from core import schema
from plugins.notepad import Sheet


class SheetSchema(schema.SQLAlchemyAutoSchema):
    class Meta:
        model = Sheet
