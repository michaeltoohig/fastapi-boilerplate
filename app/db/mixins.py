
from sqlalchemy import Column
from sqlalchemy_utc import UtcDateTime, utcnow


class TimeMixin(object):
    """A mixin that adds ``created_at`` and ``updated_at`` columns to any declarative-mapped class."""

    __table_args__ = {'extend_existing': True}

    created_at = Column(UtcDateTime(), nullable=False, default=utcnow())
    updated_at = Column(UtcDateTime(), nullable=False, default=utcnow(), onupdate=utcnow())

