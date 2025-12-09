import os
import random
from datetime import datetime, timezone
import psycopg2
from time import sleep

DB_URL = os.getenv("DB_URL", "postgresql://traffic:traffic@db:5432/trafficdb")

segments = [
    (1, "Jarry → Pointe-à-Pitre"),
    (2, "Abymes → Pointe-à-Pitre"),
    (3, "Gosier → Pointe-à-Pitre"),
]

def simulate(conn):
    now = datetime.now(timezone.utc)

    with conn.cursor() as cur:
        for seg_id, name in segments:
            speed = random.randint(10, 80)
            congestion = 100 - speed

            cur.execute("""
                INSERT INTO traffic_measurements
                (segment_id, timestamp, avg_speed_kmh, congestion_level)
                VALUES (%s, %s, %s, %s)
            """, (seg_id, now, speed, congestion))

    conn.commit()
    print(f"[SIMULATOR] batch inserted at {now}")

def main():
    conn = None
    while True:
        try:
            if conn is None:
                conn = psycopg2.connect(DB_URL)

            simulate(conn)
            sleep(60)

        except Exception as e:
            print("Error:", e)
            conn = None
            sleep(5)

if __name__ == "__main__":
    main()