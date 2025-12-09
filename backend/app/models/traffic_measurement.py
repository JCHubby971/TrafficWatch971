from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from app.db.base import Base

class TrafficMeasurement(Base):
    __tablename__ = "traffic_measurements"

    id = Column(Integer, primary_key=True)
    segment_id = Column(Integer, ForeignKey("traffic_segments.id"))
    timestamp = Column(DateTime)
    avg_speed_kmh = Column(Float)
    congestion_level = Column(Integer)