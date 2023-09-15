from db.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship

class Event(Base):
    __tablename__ = 'events'

    event_id =  Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    date = Column(DateTime, nullable = False)
    time = Column(Time)
    location = Column(String)
    description = Column(String)

    #Define the relationship with bookings
    bookings = relationship('Booking', back_populates = 'event')