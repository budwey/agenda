from config import Schema
from flask import request
from marshmallow import fields
from .. import Sheet


class SheetSchema(Schema):
    class Meta:
        model = Sheet
        load_instance = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.Date()
    last_date = fields.Date()
    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime()

    task_ids = fields.List(fields.Integer(), dump_only=True)
    entry_ids = fields.List(fields.Integer(), dump_only=True)
