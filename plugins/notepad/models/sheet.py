from datetime import datetime, timedelta, timezone
from core import db


class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date)
    last_date = db.Column(db.Date)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime, onupdate=datetime.now)
    deleted = db.Column(db.DateTime, nullable=True)

    task_ids = db.relationship('Task', backref='sheet', lazy=True)
    entry_ids = db.relationship('Entry', backref='sheet', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.date = datetime.now(timezone.utc).date() + timedelta(days=1)
        self.last_date = datetime.now(timezone.utc).date()
        self.created = datetime.now(timezone.utc)

    @db.validates('date')
    def update_name(self, key, date):
        self.name = default_sheet_name(date, self.name)
        return date


def default_sheet_name(date, name):
    if not name:
        day_name = date.strftime('%A')
        day_number = date.day
        return f"{day_number} - {day_name}"
    return name
