from . import db
from datetime import datetime, timezone

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default="created")
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
