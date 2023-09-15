from db.db import Base
from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key = True)
    username = Column(String, unique = True, nullable = False)
    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    