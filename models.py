"""Database models for the eavesdropper application."""

import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Source(db.Model):

    __tablename__ = 'source'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

class Mention(db.Model):
    """A Mention from a particular source."""

    __tablename__ = 'mention'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_id = db.Column(db.String)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    source = db.relationship(Source)
    text = db.Column(db.String)
    associated_user = db.Column(db.String)
    seen = db.Column(db.Boolean, default=False)
    recorded_at = db.Column(db.DateTime, default=datetime.datetime.now)
    occurred_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __str__(self):
        """Return the string representation of a mention."""
        return self.text

    def to_json(self):
        return {
                'id': self.id,
                'domain_id': self.domain_id,
                'source': self.source.name,
                'text': self.text,
                'associated_user': self.associated_user,
                'seen': self.seen,
                'recorded_at': str(self.recorded_at),
                'occurred_at': str(self.occurred_at)}

