from db.db import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Genre(Base):
    __tablename__ = "genres"

    genre_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship with Event
    events = relationship("Event", secondary="event_genres", back_populates="genres")

    # Many-to-Many association table for event and genre
    event_genres = Table(
        "event_genres",
        Base.metadata,
        Column("event_id", Integer, ForeignKey("events.event_id")),
        Column("genre_id", Integer, ForeignKey("genres.genre_id")),
    )
