from db.db import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    event_id = Column(Integer, ForeignKey('events.event_id'))
    ticket_id = Column(Integer, ForeignKey('tickets.ticket_id'))
    booking_date = Column(DateTime, default=datetime.utcnow)

    # Define the relationships
    user = relationship('User', back_populates='bookings')
    event = relationship('Event', back_populates='bookings')
    ticket = relationship('Ticket')