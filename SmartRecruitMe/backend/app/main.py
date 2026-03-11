from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import auth_router, candidates_router, recruiters_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartRecruitMe API",
    description="Plateforme intelligente de recrutement avec analyse CV et GitHub",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(candidates_router)
app.include_router(recruiters_router)

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
