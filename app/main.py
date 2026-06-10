from fastapi import FastAPI

from app.db.database import engine
from app.db.models import Base

from app.api.chat import router as chat_router
from app.api.catalog import router as catalog_router
from app.api.health import router as health_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Persistent Sales Assistant")

app.include_router(chat_router)
app.include_router(catalog_router)
app.include_router(health_router)


@app.get("/")
def root():

    return {
        "message": "Persistent Sales Assistant Running"
    }