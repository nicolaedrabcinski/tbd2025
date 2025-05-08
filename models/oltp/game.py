from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(String, primary_key=True)
    home_team = Column(String)
    away_team = Column(String)
    scheduled = Column(DateTime)