from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

class Artist(Base):
    __tablename__ = 'artists'

    artist_id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)

    events = relationship('Event', secondary = 'event_artist', back_populates = 'artists')

    # Many to Many Association table for event and artist
    event_artists = Table('event_artists', Base.metadata,
                          Column('event_id', Integer, ForeignKey('events.event_id')),
                          Column('artist_id', Integer, ForeignKey('artists.artist_id')))