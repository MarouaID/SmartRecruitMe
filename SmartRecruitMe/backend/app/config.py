from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./smartrecruitme.db"
    REDIS_URL: str = "redis://localhost:6379/0"
    SECRET_KEY: str = "your-secret-key-change-in-production-2024"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    GITHUB_TOKEN: str = ""
    
    # Email Configuration
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    FROM_EMAIL: str = ""
    FROM_NAME: str = "SmartRecruitMe"
    
    class Config:
        env_file = ".env"

settings = Settings()
