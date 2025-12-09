from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.db.init_db import init_db

app = FastAPI(
    title="TrafficWatch971 API",
    version="0.1.0"
)

# CORS – permettre à une page (file:// ou http://localhost:XXX) de consommer l'API
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:5173",   # si tu fais un vrai frontend plus tard
    "http://127.0.0.1:5500",   # si tu utilises Live Server ou autre
    # Tu peux ajouter d'autres origines précises ici
    # Pour le dev, on autorise tout avec "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # pour le dev : on ouvre à tout le monde
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    # Crée les tables et insère les segments par défaut
    init_db()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(api_router)