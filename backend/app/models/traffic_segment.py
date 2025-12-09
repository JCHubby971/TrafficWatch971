from sqlalchemy import Column, Integer, String
from app.db.base import Base

class TrafficSegment(Base):
    __tablename__ = "traffic_segments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)