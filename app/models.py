from app import db
from datetime import datetime


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<test[{self.id}, {self.date_posted}]>"
