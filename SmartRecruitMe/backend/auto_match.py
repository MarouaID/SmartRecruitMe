"""
Script pour lancer le matching automatique de tous les candidats avec toutes les offres
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, JobOffer, CVAnalysis
from app.orchestrator import Orchestrator

def auto_match_all():
    db = SessionLocal()
    orchestrator = Orchestrator()
    
    try:
        print("🔍 Recherche des candidats et offres...\n")
        
        # Récupérer tous les candidats avec CV analysé
        candidates = db.query(Candidate).all()
        candidates_with_cv = []
        
        for candidate in candidates:
            cv_analysis = db.query(CVAnalysis).filter(
                CVAnalysis.candidate_id == candidate.id
            ).first()
            if cv_analysis:
                candidates_with_cv.append(candidate)
        
        # Récupérer toutes les offres actives
        job_offers = db.query(JobOffer).filter(JobOffer.is_active == True).all()
        
        print(f"📊 Candidats avec CV: {len(candidates_with_cv)}")
        print(f"📊 Offres actives: {len(job_offers)}\n")
        
        if not candidates_with_cv:
            print("⚠️  Aucun candidat avec CV analysé trouvé")
            return
        
        if not job_offers:
            print("⚠️  Aucune offre active trouvée")
            return
        
        print("🚀 Lancement du matching...\n")
        
        total_matches = 0
        for job_offer in job_offers:
            print(f"📌 Offre: {job_offer.title}")
            matched_for_job = 0
            
            for candidate in candidates_with_cv:
                try:
                    result = orchestrator.match_candidate_to_job(
                        candidate.id, 
                        job_offer.id, 
                        db
                    )
                    if result:
                        matched_for_job += 1
                        total_matches += 1
                        print(f"   ✓ {candidate.full_name}: {result.get('final_score', 0):.1f}%")
                except Exception as e:
                    print(f"   ✗ Erreur pour {candidate.full_name}: {e}")
            
            print(f"   Total: {matched_for_job} candidats matchés\n")
        
        print(f"✅ Matching terminé!")
        print(f"📊 Total: {total_matches} matchings créés")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    auto_match_all()
