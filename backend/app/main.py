from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="TrafficWatch971 API",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(api_router)