from db.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = 'roles'

    role_id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)
    description = Column(String)

    # Define the relationship with the user
    users = relationship('User', back_populates = 'role')