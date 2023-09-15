from db.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Venue(Base):
    __tablename__ = 'venues'

    venue_id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    address = Column(String)
    capacity = Column(Integer)

    #Define the relationship with event
    events = relationship('Event', back_populates = 'venue')