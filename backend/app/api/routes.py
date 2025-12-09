from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.schemas.traffic import TrafficMeasurementOut
from app.models.traffic_measurement import TrafficMeasurement
from app.models.traffic_segment import TrafficSegment

router = APIRouter(prefix="/traffic", tags=["Traffic"])

@router.get("/latest", response_model=list[TrafficMeasurementOut])
def get_latest(db: Session = Depends(get_db)):
    now = datetime.utcnow()
    cutoff = now - timedelta(minutes=5)

    rows = (
        db.query(TrafficMeasurement, TrafficSegment)
        .join(TrafficSegment, TrafficMeasurement.segment_id == TrafficSegment.id)
        .filter(TrafficMeasurement.timestamp >= cutoff)
        .all()
    )

    result = []
    for tm, seg in rows:
        result.append(
            TrafficMeasurementOut(
                segment_name=seg.name,
                avg_speed_kmh=tm.avg_speed_kmh,
                congestion_level=tm.congestion_level,
                timestamp=tm.timestamp,
            )
        )
    return result