from typing import Dict
from sqlalchemy.orm import Session
from app.agents import CVAgent, GitHubAgent, MatchingAgent
from app.models import Candidate, CVAnalysis, GitHubAnalysis, MatchResult, JobOffer

class Orchestrator:
    def __init__(self):
        self.cv_agent = CVAgent()
        self.github_agent = GitHubAgent()
        self.matching_agent = MatchingAgent()
    
    def analyze_candidate_profile(self, candidate_id: int, cv_path: str, 
                                  github_username: str, db: Session) -> Dict:
        results = {
            "candidate_id": candidate_id,
            "cv_analysis": {"status": "pending"},
            "github_analysis": {"status": "pending"},
            "overall_status": "processing"
        }
        
        # Analyze CV
        if cv_path:
            cv_result = self.cv_agent.analyze(cv_path)
            results["cv_analysis"] = cv_result
            
            if cv_result["status"] == "done":
                cv_analysis = CVAnalysis(
                    candidate_id=candidate_id,
                    raw_text=cv_result.get("raw_text", ""),
                    skills=cv_result.get("skills", []),
                    experience_years=cv_result.get("experience_years", 0),
                    education=cv_result.get("education", []),
                    certifications=[],
                    languages=[],
                    cv_score=cv_result.get("cv_score", 0),
                    confidence_score=cv_result.get("confidence_score", 0)
                )
                
                existing = db.query(CVAnalysis).filter(
                    CVAnalysis.candidate_id == candidate_id
                ).first()
                
                if existing:
                    db.delete(existing)
                
                db.add(cv_analysis)
                db.commit()
        
        # Analyze GitHub
        if github_username:
            github_result = self.github_agent.analyze(github_username)
            results["github_analysis"] = github_result
            
            if github_result["status"] == "done":
                github_analysis = GitHubAnalysis(
                    candidate_id=candidate_id,
                    top_languages=github_result.get("top_languages", []),
                    total_repos=github_result.get("total_repos", 0),
                    total_commits=github_result.get("total_commits", 0),
                    regularity_score=github_result.get("regularity_score", 0),
                    collaboration_score=github_result.get("collaboration_score", 0),
                    project_quality_score=github_result.get("project_quality_score", 0),
                    inferred_softskills=github_result.get("inferred_softskills", []),
                    github_score=github_result.get("github_score", 0)
                )
                
                existing = db.query(GitHubAnalysis).filter(
                    GitHubAnalysis.candidate_id == candidate_id
                ).first()
                
                if existing:
                    db.delete(existing)
                
                db.add(github_analysis)
                db.commit()
        
        results["overall_status"] = "completed"
        return results
    
    def match_candidate_to_job(self, candidate_id: int, job_offer_id: int, 
                               db: Session) -> Dict:
        candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
        if not candidate:
            return {"status": "error", "message": "Candidate not found"}
        
        job_offer = db.query(JobOffer).filter(JobOffer.id == job_offer_id).first()
        if not job_offer:
            return {"status": "error", "message": "Job offer not found"}
        
        cv_analysis = db.query(CVAnalysis).filter(
            CVAnalysis.candidate_id == candidate_id
        ).first()
        
        github_analysis = db.query(GitHubAnalysis).filter(
            GitHubAnalysis.candidate_id == candidate_id
        ).first()
        
        candidate_data = {
            "cv_score": cv_analysis.cv_score if cv_analysis else 0,
            "github_score": github_analysis.github_score if github_analysis else 0,
            "skills": cv_analysis.skills if cv_analysis else [],
            "experience_years": cv_analysis.experience_years if cv_analysis else 0
        }
        
        job_data = {
            "required_skills": job_offer.required_skills,
            "experience_required": job_offer.experience_required,
            "description": job_offer.description
        }
        
        match_result = self.matching_agent.analyze(candidate_data, job_data)
        
        if match_result["status"] == "done":
            match_record = MatchResult(
                candidate_id=candidate_id,
                job_offer_id=job_offer_id,
                cv_match_score=match_result["cv_match_score"],
                github_match_score=match_result["github_match_score"],
                semantic_match_score=match_result["semantic_match_score"],
                final_score=match_result["final_score"],
                matched_skills=match_result["matched_skills"],
                missing_skills=match_result["missing_skills"],
                score_breakdown=match_result["score_breakdown"]
            )
            
            existing = db.query(MatchResult).filter(
                MatchResult.candidate_id == candidate_id,
                MatchResult.job_offer_id == job_offer_id
            ).first()
            
            if existing:
                db.delete(existing)
            
            db.add(match_record)
            db.commit()
        
        return match_result
    
    def get_candidate_matches_for_job(self, job_offer_id: int, db: Session) -> list:
        matches = db.query(MatchResult).filter(
            MatchResult.job_offer_id == job_offer_id
        ).order_by(MatchResult.final_score.desc()).all()
        
        results = []
        for match in matches:
            candidate = db.query(Candidate).filter(
                Candidate.id == match.candidate_id
            ).first()
            
            if not candidate:
                continue
            
            cv_analysis = db.query(CVAnalysis).filter(
                CVAnalysis.candidate_id == candidate.id
            ).first()
            
            github_analysis = db.query(GitHubAnalysis).filter(
                GitHubAnalysis.candidate_id == candidate.id
            ).first()
            
            results.append({
                "candidate_id": candidate.id,
                "candidate_name": candidate.full_name,
                "job_offer_id": job_offer_id,
                "final_score": match.final_score,
                "cv_score": cv_analysis.cv_score if cv_analysis else 0,
                "github_score": github_analysis.github_score if github_analysis else 0,
                "matching_score": match.semantic_match_score,
                "matched_skills": match.matched_skills,
                "missing_skills": match.missing_skills,
                "github_highlights": {
                    "top_languages": github_analysis.top_languages if github_analysis else [],
                    "regularity": "Très bonne" if github_analysis and github_analysis.regularity_score > 0.7 else "Bonne" if github_analysis and github_analysis.regularity_score > 0.4 else "Moyenne",
                    "projects_count": github_analysis.total_repos if github_analysis else 0
                },
                "agents_status": {
                    "cv_agent": "done" if cv_analysis else "pending",
                    "github_agent": "done" if github_analysis else "pending",
                    "matching_agent": "done",
                    "report_agent": "done"
                }
            })
        
        return results
