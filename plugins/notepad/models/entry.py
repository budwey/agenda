from core import db
from datetime import datetime, timezone


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True, default=None)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, nullable=False, default=0)
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    modified = db.Column(db.DateTime, default=datetime.now(timezone.utc),
                         onupdate=datetime.now(timezone.utc))
    deleted = db.Column(db.DateTime, nullable=True)

    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=True,
                         default=None)
    sheet_id = db.Column(db.Integer, db.ForeignKey('sheet.id'))
