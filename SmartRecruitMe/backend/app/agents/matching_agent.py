from typing import Dict, List
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class MatchingAgent:
    def __init__(self):
        pass
    
    def calculate_skill_match(self, candidate_skills: List[str], 
                             required_skills: List[str]) -> Dict:
        if not candidate_skills or not required_skills:
            return {
                "score": 0.0,
                "matched": [],
                "missing": required_skills
            }
        
        candidate_skills_lower = [s.lower() for s in candidate_skills]
        required_skills_lower = [s.lower() for s in required_skills]
        
        matched = []
        missing = []
        
        for req_skill in required_skills:
            if req_skill.lower() in candidate_skills_lower:
                matched.append(req_skill)
            else:
                missing.append(req_skill)
        
        match_ratio = len(matched) / len(required_skills) if required_skills else 0
        
        return {
            "score": round(match_ratio * 100, 2),
            "matched": matched,
            "missing": missing
        }
    
    def calculate_experience_match(self, candidate_exp: int, required_exp: int) -> float:
        if required_exp == 0:
            return 100.0
        
        if candidate_exp >= required_exp:
            return 100.0
        
        ratio = candidate_exp / required_exp
        return round(ratio * 100, 2)
    
    def semantic_similarity(self, text1: str, text2: str) -> float:
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        jaccard = len(intersection) / len(union) if union else 0
        
        return round(jaccard * 100, 2)
    
    def calculate_final_score(self, cv_score: float, github_score: float, 
                             skill_match: float, exp_match: float) -> Dict:
        weights = {
            "cv": 0.25,
            "github": 0.25,
            "skills": 0.35,
            "experience": 0.15
        }
        
        final_score = (
            cv_score * weights["cv"] +
            github_score * weights["github"] +
            skill_match * weights["skills"] +
            exp_match * weights["experience"]
        )
        
        breakdown = {
            "cv_contribution": round(cv_score * weights["cv"], 2),
            "github_contribution": round(github_score * weights["github"], 2),
            "skills_contribution": round(skill_match * weights["skills"], 2),
            "experience_contribution": round(exp_match * weights["experience"], 2)
        }
        
        return {
            "final_score": round(final_score, 2),
            "breakdown": breakdown
        }
    
    def analyze(self, candidate_data: Dict, job_offer_data: Dict) -> Dict:
        cv_score = candidate_data.get("cv_score", 0)
        github_score = candidate_data.get("github_score", 0)
        candidate_skills = candidate_data.get("skills", [])
        candidate_exp = candidate_data.get("experience_years", 0)
        
        required_skills = job_offer_data.get("required_skills", [])
        required_exp = job_offer_data.get("experience_required", 0)
        job_description = job_offer_data.get("description", "")
        
        skill_match_result = self.calculate_skill_match(candidate_skills, required_skills)
        exp_match = self.calculate_experience_match(candidate_exp, required_exp)
        
        candidate_text = " ".join(candidate_skills)
        semantic_score = self.semantic_similarity(candidate_text, job_description)
        
        final_result = self.calculate_final_score(
            cv_score,
            github_score,
            skill_match_result["score"],
            exp_match
        )
        
        return {
            "agent": "MATCHING_AGENT",
            "status": "done",
            "cv_match_score": cv_score,
            "github_match_score": github_score,
            "skill_match_score": skill_match_result["score"],
            "experience_match_score": exp_match,
            "semantic_match_score": semantic_score,
            "final_score": final_result["final_score"],
            "matched_skills": skill_match_result["matched"],
            "missing_skills": skill_match_result["missing"],
            "score_breakdown": final_result["breakdown"]
        }
