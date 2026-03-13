"""
Script pour créer des analyses GitHub mockées pour tous les candidats
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, GitHubAnalysis, User
from app.orchestrator import Orchestrator

def create_mock_github_analysis():
    db = SessionLocal()
    orchestrator = Orchestrator()
    
    try:
        print("🔧 Création des analyses GitHub mockées...\n")
        
        candidates = db.query(Candidate).all()
        
        for candidate in candidates:
            user = db.query(User).filter(User.id == candidate.user_id).first()
            
            print(f"📊 {candidate.full_name} ({user.email if user else 'N/A'})")
            print(f"   GitHub: {candidate.github_username}")
            
            if candidate.github_username:
                try:
                    # Lancer l'analyse avec les données mockées
                    result = orchestrator.analyze_candidate_profile(
                        candidate_id=candidate.id,
                        cv_path=candidate.cv_path,
                        github_username=candidate.github_username,
                        db=db
                    )
                    
                    if result.get("github_analysis", {}).get("status") == "done":
                        github_data = result["github_analysis"]
                        print(f"   ✅ Analyse créée!")
                        print(f"      Score: {github_data.get('github_score', 0)}%")
                        print(f"      Repos: {github_data.get('total_repos', 0)}")
                        print(f"      Languages: {', '.join(github_data.get('top_languages', [])[:3])}")
                    else:
                        print(f"   ⚠️  Status: {result.get('github_analysis', {}).get('status', 'unknown')}")
                        
                except Exception as e:
                    print(f"   ❌ Erreur: {e}")
            else:
                print(f"   ⚠️  Pas de username GitHub")
            
            print()
        
        print("=" * 70)
        print("\n✅ Analyses GitHub créées!")
        print("\n📝 Vous pouvez maintenant:")
        print("   1. Vous connecter avec n'importe quel compte candidat")
        print("   2. Voir les scores GitHub dans le profil")
        print("   3. Les offres compatibles sont mises à jour")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_mock_github_analysis()
