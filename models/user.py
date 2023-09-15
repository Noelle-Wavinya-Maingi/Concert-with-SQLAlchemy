from db.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key = True)
    username = Column(String, unique = True, nullable = False)
    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    role_id = Column(Integer,ForeignKey("roles.role_id"))

# Define the relationships
    role = relationship('Role', back_populates = 'users')
    