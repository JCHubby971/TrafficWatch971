from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import get_db
from app.schemas.traffic import TrafficMeasurementOut
from app.models.traffic_measurement import TrafficMeasurement
from app.models.traffic_segment import TrafficSegment

router = APIRouter(prefix="/traffic", tags=["Traffic"])

@router.get("/latest", response_model=list[TrafficMeasurementOut])
def get_latest(db: Session = Depends(get_db)):
    # Sous-requête : dernière timestamp par segment
    subq = (
        db.query(
            TrafficMeasurement.segment_id,
            func.max(TrafficMeasurement.timestamp).label("max_ts"),
        )
        .group_by(TrafficMeasurement.segment_id)
        .subquery()
    )

    # Jointure pour récupérer la ligne complète correspondante
    rows = (
        db.query(TrafficMeasurement, TrafficSegment)
        .join(
            subq,
            (TrafficMeasurement.segment_id == subq.c.segment_id)
            & (TrafficMeasurement.timestamp == subq.c.max_ts),
        )
        .join(TrafficSegment, TrafficMeasurement.segment_id == TrafficSegment.id)
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