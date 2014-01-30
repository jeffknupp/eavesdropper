"""Database models for the eavesdropper application."""

import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Source(Base):

    __tablename__ = 'source'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

class Mention(Base):
    """A Mention from a particular source."""

    __tablename__ = 'mention'
    id = Column(Integer, primary_key=True, autoincrement=True)
    domain_id = Column(String)
    source_id = Column(Integer, ForeignKey('source.id'))
    source = relationship(Source)
    text = Column(String)
    associated_user = Column(String)
    seen = Column(Boolean, default=False)
    recorded_at = Column(DateTime, default=datetime.datetime.now)
    occurred_at = Column(DateTime, default=datetime.datetime.now)

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

