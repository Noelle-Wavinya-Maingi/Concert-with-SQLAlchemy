from db.db import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.event_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    amount = Column(Float, nullable=False)
    
    # Define the relationship with Event and User
    event = relationship('Event', back_populates='payments')
    user = relationship('User', back_populates='payments')