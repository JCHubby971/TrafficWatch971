# backend/app/db/init_db.py
from sqlalchemy.orm import Session

from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.traffic_segment import TrafficSegment
from app.models.traffic_measurement import TrafficMeasurement  # important pour créer la table


def init_db() -> None:
    """
    Initialise la base :
    - crée toutes les tables connues du Base
    - insère quelques segments par défaut si nécessaire
    """
    # Crée toutes les tables (si elles n'existent pas déjà)
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        # Vérifie si on a déjà des segments
        count = db.query(TrafficSegment).count()
        if count == 0:
            segments = [
                TrafficSegment(id=1, name="Jarry → Pointe-à-Pitre"),
                TrafficSegment(id=2, name="Abymes → Pointe-à-Pitre"),
                TrafficSegment(id=3, name="Gosier → Pointe-à-Pitre"),
            ]
            db.add_all(segments)
            db.commit()
    finally:
        db.close()