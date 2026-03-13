from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import (
    auth_router,
    candidates_router,
    recruiters_router,
    chat_router,
    notifications_router,
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartRecruitMe API",
    description="Plateforme intelligente de recrutement avec analyse CV et GitHub",
    version="1.0.0"
)

# Include routers FIRST
app.include_router(auth_router)
app.include_router(candidates_router)
app.include_router(recruiters_router)
app.include_router(chat_router)
app.include_router(notifications_router)

# CORS configuration AFTER routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SmartRecruitMe API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
