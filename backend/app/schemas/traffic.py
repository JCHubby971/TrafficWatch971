from pydantic import BaseModel
from datetime import datetime

class TrafficMeasurementOut(BaseModel):
    segment_name: str
    avg_speed_kmh: float
    congestion_level: int
    timestamp: datetime

    class Config:
        orm_mode = True