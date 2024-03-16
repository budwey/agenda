from core import db


class Sheet(db.Model):
    __tablename__ = 'notepad'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
