from .import db
from datetime import datetime


class EmployClockings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f'Signed in @: {self.location} {self.date_posted}'
