"""
Script pour créer uniquement les analyses GitHub (sans toucher aux CV)
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, GitHubAnalysis
from app.agents.github_agent import GitHubAgent

def create_github_only():
    db = SessionLocal()
    agent = GitHubAgent()
    
    try:
        print("🔧 Création des analyses GitHub...\n")
        
        candidates = db.query(Candidate).all()
        
        for candidate in candidates:
            print(f"📊 {candidate.full_name}")
            print(f"   GitHub: {candidate.github_username}")
            
            if not candidate.github_username:
                print(f"   ⚠️  Pas de username GitHub\n")
                continue
            
            # Vérifier si une analyse existe déjà
            existing = db.query(GitHubAnalysis).filter(
                GitHubAnalysis.candidate_id == candidate.id
            ).first()
            
            if existing:
                print(f"   ℹ️  Analyse existante - Suppression...")
                db.delete(existing)
                db.commit()
            
            # Analyser avec les données mockées
            try:
                result = agent.analyze(candidate.github_username)
                
                if result.get("status") == "done":
                    github_analysis = GitHubAnalysis(
                        candidate_id=candidate.id,
                        top_languages=result.get("top_languages", []),
                        total_repos=result.get("total_repos", 0),
                        total_commits=result.get("total_commits", 0),
                        regularity_score=result.get("regularity_score", 0),
                        collaboration_score=result.get("collaboration_score", 0),
                        project_quality_score=result.get("project_quality_score", 0),
                        inferred_softskills=result.get("inferred_softskills", []),
                        github_score=result.get("github_score", 0)
                    )
                    
                    db.add(github_analysis)
                    db.commit()
                    
                    print(f"   ✅ Analyse créée!")
                    print(f"      Score: {result.get('github_score', 0)}%")
                    print(f"      Repos: {result.get('total_repos', 0)}")
                    print(f"      Languages: {', '.join(result.get('top_languages', [])[:3])}")
                else:
                    print(f"   ❌ Erreur: {result.get('message', 'Unknown')}")
                    
            except Exception as e:
                print(f"   ❌ Exception: {e}")
                db.rollback()
            
            print()
        
        print("=" * 70)
        print("\n✅ Analyses GitHub créées!")
        print("\n📝 Maintenant:")
        print("   1. Connectez-vous avec un compte candidat")
        print("   2. Les scores GitHub sont visibles dans le profil")
        print("   3. Pas besoin de cliquer sur 'Analyser GitHub'")
        
    except Exception as e:
        print(f"❌ Erreur globale: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    create_github_only()
