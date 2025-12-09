from sqlalchemy import Column, Integer, String
from app.db.session import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TrafficSegment(Base):
    __tablename__ = "traffic_segments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)