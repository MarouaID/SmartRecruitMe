from collections import Counter
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User, Recruiter, JobOffer, Candidate, CVAnalysis, GitHubAnalysis, MatchResult, Notification
from app.schemas import JobOfferCreate, JobOfferResponse
from app.auth import get_current_recruiter
from app.orchestrator import Orchestrator

router = APIRouter(prefix="/api/recruiters", tags=["Recruiters"])
orchestrator = Orchestrator()

@router.post("/job-offers", response_model=JobOfferResponse)
def create_job_offer(
    job_data: JobOfferCreate,
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")
    
    new_job = JobOffer(
        recruiter_id=recruiter.id,
        title=job_data.title,
        description=job_data.description,
        required_skills=job_data.required_skills,
        experience_required=job_data.experience_required,
        location=job_data.location,
        salary_range=job_data.salary_range,
        contract_type=job_data.contract_type
    )
    
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    
    return new_job

@router.get("/job-offers", response_model=List[JobOfferResponse])
def get_my_job_offers(
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")
    
    jobs = db.query(JobOffer).filter(JobOffer.recruiter_id == recruiter.id).all()
    return jobs

@router.get("/job-offers/{job_id}/candidates")
def get_candidates_for_job(
    job_id: int,
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")
    
    job_offer = db.query(JobOffer).filter(
        JobOffer.id == job_id,
        JobOffer.recruiter_id == recruiter.id
    ).first()
    
    if not job_offer:
        raise HTTPException(status_code=404, detail="Job offer not found")
    
    results = orchestrator.get_candidate_matches_for_job(job_id, db)
    return results

@router.post("/job-offers/{job_id}/match-candidates")
def match_all_candidates_to_job(
    job_id: int,
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")
    
    job_offer = db.query(JobOffer).filter(
        JobOffer.id == job_id,
        JobOffer.recruiter_id == recruiter.id
    ).first()
    
    if not job_offer:
        raise HTTPException(status_code=404, detail="Job offer not found")
    
    candidates = db.query(Candidate).all()
    
    matched_count = 0
    for candidate in candidates:
        cv_analysis = db.query(CVAnalysis).filter(
            CVAnalysis.candidate_id == candidate.id
        ).first()
        
        if cv_analysis:
            orchestrator.match_candidate_to_job(candidate.id, job_id, db)
            matched_count += 1

    # Create a notification for the recruiter
    notification = Notification(
        user_id=current_user.id,
        message=f"Votre matching pour l'offre '{job_offer.title}' a été exécuté avec {matched_count} candidats évalués.",
    )
    db.add(notification)
    db.commit()
    
    return {
        "message": f"Matched {matched_count} candidates to job offer",
        "job_id": job_id,
        "matched_count": matched_count
    }

@router.get("/candidates/{candidate_id}")
def get_candidate_detail(
    candidate_id: int,
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    cv_analysis = db.query(CVAnalysis).filter(CVAnalysis.candidate_id == candidate.id).first()
    github_analysis = db.query(GitHubAnalysis).filter(GitHubAnalysis.candidate_id == candidate.id).first()
    
    return {
        "id": candidate.id,
        "full_name": candidate.full_name,
        "email": candidate.user.email,
        "github_username": candidate.github_username,
        "location": candidate.location,
        "phone": candidate.phone,
        "cv_analysis": {
            "skills": cv_analysis.skills if cv_analysis else [],
            "experience_years": cv_analysis.experience_years if cv_analysis else 0,
            "education": cv_analysis.education if cv_analysis else [],
            "cv_score": cv_analysis.cv_score if cv_analysis else 0,
            "confidence_score": cv_analysis.confidence_score if cv_analysis else 0
        } if cv_analysis else None,
        "github_analysis": {
            "top_languages": github_analysis.top_languages if github_analysis else [],
            "total_repos": github_analysis.total_repos if github_analysis else 0,
            "total_commits": github_analysis.total_commits if github_analysis else 0,
            "regularity_score": github_analysis.regularity_score if github_analysis else 0,
            "collaboration_score": github_analysis.collaboration_score if github_analysis else 0,
            "project_quality_score": github_analysis.project_quality_score if github_analysis else 0,
            "inferred_softskills": github_analysis.inferred_softskills if github_analysis else [],
            "github_score": github_analysis.github_score if github_analysis else 0
        } if github_analysis else None
    }

@router.get("/dashboard/analytics")
def get_dashboard_analytics(
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")

    match_results = (
        db.query(MatchResult)
        .join(JobOffer)
        .filter(JobOffer.recruiter_id == recruiter.id)
        .all()
    )

    # Applications over time (based on match result creation date)
    counts = Counter((m.created_at.date() for m in match_results if m.created_at))
    applications_over_time = [
        {"date": d.isoformat(), "count": c} for d, c in sorted(counts.items())
    ]

    # Average scores
    avg_score = (
        sum((m.final_score or 0) for m in match_results) / max(len(match_results), 1)
        if match_results
        else 0
    )

    # Top skills in the candidate pool
    skill_counts: Counter = Counter()
    for m in match_results:
        if m.matched_skills:
            skill_counts.update([s for s in m.matched_skills if isinstance(s, str)])

    top_skills = [
        {"skill": skill, "count": count}
        for skill, count in skill_counts.most_common(10)
    ]

    return {
        "applications_over_time": applications_over_time,
        "average_score": round(avg_score, 2),
        "top_skills": top_skills,
    }


@router.get("/dashboard/stats")
def get_dashboard_stats(
    current_user: User = Depends(get_current_recruiter),
    db: Session = Depends(get_db)
):
    recruiter = db.query(Recruiter).filter(Recruiter.user_id == current_user.id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter profile not found")
    
    total_jobs = db.query(JobOffer).filter(JobOffer.recruiter_id == recruiter.id).count()
    active_jobs = db.query(JobOffer).filter(
        JobOffer.recruiter_id == recruiter.id,
        JobOffer.is_active == 1
    ).count()
    
    total_candidates = db.query(Candidate).count()
    
    return {
        "total_job_offers": total_jobs,
        "active_job_offers": active_jobs,
        "total_candidates": total_candidates
    }
