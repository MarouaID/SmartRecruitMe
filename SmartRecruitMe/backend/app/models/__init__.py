from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, ForeignKey, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

class UserRole(str, enum.Enum):
    CANDIDATE = "candidate"
    RECRUITER = "recruiter"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="user", uselist=False)
    recruiter = relationship("Recruiter", back_populates="user", uselist=False)

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    full_name = Column(String(255), nullable=False)
    github_username = Column(String(255))
    gitlab_username = Column(String(255))
    phone = Column(String(50))
    location = Column(String(255))
    cv_path = Column(String(500))
    profile_picture = Column(String(500))
    
    user = relationship("User", back_populates="candidate")
    cv_analysis = relationship("CVAnalysis", back_populates="candidate", uselist=False)
    github_analysis = relationship("GitHubAnalysis", back_populates="candidate", uselist=False)
    match_results = relationship("MatchResult", back_populates="candidate")

class Recruiter(Base):
    __tablename__ = "recruiters"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    company_name = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(50))
    
    user = relationship("User", back_populates="recruiter")
    job_offers = relationship("JobOffer", back_populates="recruiter")

class JobOffer(Base):
    __tablename__ = "job_offers"
    
    id = Column(Integer, primary_key=True, index=True)
    recruiter_id = Column(Integer, ForeignKey("recruiters.id"))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    required_skills = Column(JSON)
    experience_required = Column(Integer, default=0)
    location = Column(String(255))
    salary_range = Column(String(100))
    contract_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Integer, default=1)
    
    recruiter = relationship("Recruiter", back_populates="job_offers")
    match_results = relationship("MatchResult", back_populates="job_offer")

class CVAnalysis(Base):
    __tablename__ = "cv_analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), unique=True)
    raw_text = Column(Text)
    skills = Column(JSON)
    experience_years = Column(Integer)
    education = Column(JSON)
    certifications = Column(JSON)
    languages = Column(JSON)
    cv_score = Column(Float)
    confidence_score = Column(Float)
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="cv_analysis")

class GitHubAnalysis(Base):
    __tablename__ = "github_analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), unique=True)
    top_languages = Column(JSON)
    total_repos = Column(Integer)
    total_commits = Column(Integer)
    regularity_score = Column(Float)
    collaboration_score = Column(Float)
    project_quality_score = Column(Float)
    inferred_softskills = Column(JSON)
    github_score = Column(Float)
    analyzed_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="github_analysis")

class MatchResult(Base):
    __tablename__ = "match_results"
    
    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    job_offer_id = Column(Integer, ForeignKey("job_offers.id"))
    cv_match_score = Column(Float)
    github_match_score = Column(Float)
    semantic_match_score = Column(Float)
    final_score = Column(Float)
    matched_skills = Column(JSON)
    missing_skills = Column(JSON)
    score_breakdown = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="match_results")
    job_offer = relationship("JobOffer", back_populates="match_results")
