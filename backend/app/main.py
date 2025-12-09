from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db.init_db import init_db

app = FastAPI(
    title="TrafficWatch971 API",
    version="0.1.0"
)


@app.on_event("startup")
def on_startup():
    # Crée les tables et insère les segments par défaut
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(api_router)