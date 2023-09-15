#Importations of necessary modules from sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#define the url for the sqlite db
db_url =  "sqlite:///concert.db"

#create a SQLAlchemy db engine using the defined url
engine =  create_engine(db_url)

# create a session factory that will create individual db sessions
Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)
session = Session()

# create a base class for declarative sqlalchemy models
Base = declarative_base()
