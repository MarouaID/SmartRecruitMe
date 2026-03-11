from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from app.database import get_db
from app.models import User, Candidate, CVAnalysis, GitHubAnalysis, MatchResult, JobOffer
from app.auth import get_current_candidate
from app.orchestrator import Orchestrator

router = APIRouter(prefix="/api/candidates", tags=["Candidates"])
orchestrator = Orchestrator()

UPLOAD_DIR = "uploads/cvs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-cv")
def upload_cv(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_candidate),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(('.pdf', '.docx')):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and DOCX files are allowed"
        )
    
    candidate = db.query(Candidate).filter(Candidate.user_id == current_user.id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate profile not found")
    
    file_path = os.path.join(UPLOAD_DIR, f"{candidate.id}_{file.filename}")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    candidate.cv_path = file_path
    db.commit()
    
    result = orchestrator.analyze_candidate_profile(
        candidate_id=candidate.id,
        cv_path=file_path,
        github_username=candidate.github_username,
        db=db
    )
    
    return {
        "message": "CV uploaded and analyzed successfully",
        "file_path": file_path,
        "analysis": result
    }

@router.get("/profile")
def get_profile(
    current_user: User = Depends(get_current_candidate),
    db: Session = Depends(get_db)
):
    candidate = db.query(Candidate).filter(Candidate.user_id == current_user.id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate profile not found")
    
    cv_analysis = db.query(CVAnalysis).filter(CVAnalysis.candidate_id == candidate.id).first()
    github_analysis = db.query(GitHubAnalysis).filter(GitHubAnalysis.candidate_id == candidate.id).first()
    
    return {
        "id": candidate.id,
        "full_name": candidate.full_name,
        "email": current_user.email,
        "github_username": candidate.github_username,
        "location": candidate.location,
        "phone": candidate.phone,
        "cv_analysis": {
            "skills": cv_analysis.skills if cv_analysis else [],
            "experience_years": cv_analysis.experience_years if cv_analysis else 0,
            "education": cv_analysis.education if cv_analysis else [],
            "cv_score": cv_analysis.cv_score if cv_analysis else 0
        } if cv_analysis else None,
        "github_analysis": {
            "top_languages": github_analysis.top_languages if github_analysis else [],
            "total_repos": github_analysis.total_repos if github_analysis else 0,
            "regularity_score": github_analysis.regularity_score if github_analysis else 0,
            "collaboration_score": github_analysis.collaboration_score if github_analysis else 0,
            "inferred_softskills": github_analysis.inferred_softskills if github_analysis else [],
            "github_score": github_analysis.github_score if github_analysis else 0
        } if github_analysis else None
    }

@router.get("/matching-jobs")
def get_matching_jobs(
    current_user: User = Depends(get_current_candidate),
    db: Session = Depends(get_db)
):
    candidate = db.query(Candidate).filter(Candidate.user_id == current_user.id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate profile not found")
    
    matches = db.query(MatchResult).filter(
        MatchResult.candidate_id == candidate.id
    ).order_by(MatchResult.final_score.desc()).all()
    
    results = []
    for match in matches:
        job_offer = db.query(JobOffer).filter(JobOffer.id == match.job_offer_id).first()
        if job_offer and job_offer.is_active:
            results.append({
                "job_id": job_offer.id,
                "title": job_offer.title,
                "company": job_offer.recruiter.company_name,
                "location": job_offer.location,
                "match_score": match.final_score,
                "matched_skills": match.matched_skills,
                "missing_skills": match.missing_skills,
                "required_skills": job_offer.required_skills
            })
    
    return results

@router.post("/analyze-github")
def analyze_github(
    current_user: User = Depends(get_current_candidate),
    db: Session = Depends(get_db)
):
    candidate = db.query(Candidate).filter(Candidate.user_id == current_user.id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate profile not found")
    
    if not candidate.github_username:
        raise HTTPException(status_code=400, detail="GitHub username not set")
    
    result = orchestrator.analyze_candidate_profile(
        candidate_id=candidate.id,
        cv_path=candidate.cv_path,
        github_username=candidate.github_username,
        db=db
    )
    
    return result
