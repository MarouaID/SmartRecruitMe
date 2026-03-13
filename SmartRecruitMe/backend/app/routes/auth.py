from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Optional
from app.database import get_db
from app.models import User, Candidate, Recruiter, UserRole
from app.schemas import UserCreate, UserLogin, Token, CandidateCreate, RecruiterCreate
from app.auth import verify_password, get_password_hash, create_access_token
from app.config import settings
from pydantic import BaseModel

class RegisterRequest(BaseModel):
    email: str
    password: str
    role: str
    full_name: Optional[str] = None
    github_username: Optional[str] = None
    company_name: Optional[str] = None

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/register", response_model=Token)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(data.password)
    
    new_user = User(
        email=data.email,
        hashed_password=hashed_password,
        role=UserRole(data.role)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    if data.role == "candidate" and data.full_name:
        new_candidate = Candidate(
            user_id=new_user.id,
            full_name=data.full_name,
            github_username=data.github_username
        )
        db.add(new_candidate)
        db.commit()
    
    elif data.role == "recruiter" and data.company_name and data.full_name:
        new_recruiter = Recruiter(
            user_id=new_user.id,
            company_name=data.company_name,
            full_name=data.full_name
        )
        db.add(new_recruiter)
        db.commit()
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": new_user.email, "role": new_user.role.value},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": new_user.role.value,
        "user_id": new_user.id
    }

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.email).first()
    
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role.value},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role.value,
        "user_id": user.id
    }
