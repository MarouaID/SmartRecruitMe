"""
Script pour vérifier et mettre à jour les usernames GitHub des candidats
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, User
from app.agents.github_agent import GitHubAgent

def check_and_fix_github():
    db = SessionLocal()
    agent = GitHubAgent()
    
    try:
        print("🔍 Vérification des candidats...\n")
        
        candidates = db.query(Candidate).all()
        
        for candidate in candidates:
            user = db.query(User).filter(User.id == candidate.user_id).first()
            print(f"📋 Candidat: {candidate.full_name}")
            print(f"   Email: {user.email if user else 'N/A'}")
            print(f"   GitHub actuel: {candidate.github_username or 'Non défini'}")
            
            if candidate.github_username:
                print(f"   Test du compte GitHub...")
                result = agent.analyze(candidate.github_username)
                
                if result.get("status") == "done":
                    print(f"   ✅ GitHub valide - Score: {result.get('github_score', 0)}%")
                else:
                    print(f"   ❌ Erreur: {result.get('message', 'Unknown error')}")
                    print(f"   💡 Suggestion: Utiliser un compte GitHub valide")
            else:
                print(f"   ⚠️  Pas de GitHub configuré")
            
            print()
        
        print("=" * 70)
        print("\n💡 Suggestions de comptes GitHub valides pour tester:\n")
        
        test_accounts = {
            "tj": "55% - Créateur de Express.js, nombreux projets JavaScript",
            "torvalds": "80% - Créateur de Linux",
            "gvanrossum": "85% - Créateur de Python",
            "kennethreitz": "~50-60% - Créateur de Requests (Python)",
            "mbostock": "~60-70% - Créateur de D3.js",
        }
        
        for username, desc in test_accounts.items():
            print(f"   • {username:15} - {desc}")
        
        print("\n" + "=" * 70)
        print("\n🔧 Pour mettre à jour un username GitHub:")
        print("   1. Connectez-vous sur le frontend")
        print("   2. Allez dans le profil")
        print("   3. Modifiez le username GitHub")
        print("   4. Cliquez sur 'Analyser GitHub'")
        
        print("\n   OU utilisez ce script pour mettre à jour directement:\n")
        
        # Proposer de mettre à jour
        print("📝 Voulez-vous mettre à jour les usernames maintenant?")
        print("   Candidat 'candidat@test.com' -> Suggéré: 'tj' (score ~55%)")
        
        # Mise à jour automatique pour le candidat de test
        candidate_test = db.query(Candidate).join(User).filter(
            User.email == "candidat@test.com"
        ).first()
        
        if candidate_test:
            old_username = candidate_test.github_username
            candidate_test.github_username = "tj"
            db.commit()
            print(f"\n✅ Mis à jour: {old_username or 'None'} -> 'tj'")
            print(f"   Vous pouvez maintenant cliquer sur 'Analyser GitHub' dans l'interface")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    check_and_fix_github()
