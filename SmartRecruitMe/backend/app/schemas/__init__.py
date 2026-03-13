from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    CANDIDATE = "candidate"
    RECRUITER = "recruiter"

class UserCreate(BaseModel):
    email: str
    password: str
    role: UserRole

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    user_id: int

class CandidateCreate(BaseModel):
    full_name: str
    github_username: Optional[str] = None
    gitlab_username: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None

class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: str
    github_username: Optional[str]
    location: Optional[str]
    cv_score: Optional[float]
    github_score: Optional[float]
    skills: Optional[List[str]]
    
    class Config:
        from_attributes = True

class RecruiterCreate(BaseModel):
    company_name: str
    full_name: str
    phone: Optional[str] = None

class JobOfferCreate(BaseModel):
    title: str
    description: str
    required_skills: List[str]
    experience_required: int = 0
    location: Optional[str] = None
    salary_range: Optional[str] = None
    contract_type: Optional[str] = None

class JobOfferResponse(BaseModel):
    id: int
    title: str
    description: str
    required_skills: List[str]
    experience_required: int
    location: Optional[str]
    salary_range: Optional[str]
    contract_type: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class CVAnalysisResponse(BaseModel):
    agent: str = "CV_AGENT"
    status: str
    skills: List[str]
    experience_years: int
    education: List[Dict]
    cv_score: float
    confidence_score: float

class GitHubAnalysisResponse(BaseModel):
    agent: str = "GITHUB_AGENT"
    status: str
    top_languages: List[str]
    regularity_score: float
    collaboration_score: float
    project_quality_score: float
    inferred_softskills: List[str]
    github_score: float

class MatchResultResponse(BaseModel):
    candidate_id: int
    candidate_name: str
    job_offer_id: int
    final_score: float
    cv_score: float
    github_score: float
    matching_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    github_highlights: Dict
    agents_status: Dict
    
    class Config:
        from_attributes = True

class CandidateProfileResponse(BaseModel):
    id: int
    full_name: str
    email: str
    github_username: Optional[str]
    location: Optional[str]
    cv_analysis: Optional[CVAnalysisResponse]
    github_analysis: Optional[GitHubAnalysisResponse]
    final_score: Optional[float]
    
    class Config:
        from_attributes = True


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str
