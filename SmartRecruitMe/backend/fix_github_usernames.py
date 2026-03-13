"""
Script pour corriger tous les usernames GitHub avec des comptes valides
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, User

def fix_all_github_usernames():
    db = SessionLocal()
    
    try:
        print("🔧 Correction des usernames GitHub...\n")
        
        # Mapping des candidats vers des comptes GitHub valides
        updates = [
            {
                "email": "candidat@test.com",
                "name": "Maroua Idomar",
                "github": "tj",
                "score": "~55%"
            },
            {
                "email": "aghribazar@gmail.com",
                "name": "Aghrib Azar",
                "github": "torvalds",
                "score": "~80%"
            },
            {
                "email": "oussama@gmail.com",
                "name": "Oussama Chraybi",
                "github": "gvanrossum",
                "score": "~85%"
            }
        ]
        
        for update in updates:
            user = db.query(User).filter(User.email == update["email"]).first()
            if user:
                candidate = db.query(Candidate).filter(
                    Candidate.user_id == user.id
                ).first()
                
                if candidate:
                    old_username = candidate.github_username
                    candidate.github_username = update["github"]
                    print(f"✅ {update['name']}")
                    print(f"   Email: {update['email']}")
                    print(f"   GitHub: {old_username or 'None'} -> {update['github']}")
                    print(f"   Score attendu: {update['score']}")
                    print()
        
        db.commit()
        
        print("=" * 70)
        print("\n✅ Tous les usernames GitHub ont été mis à jour!")
        print("\n📝 Vous pouvez maintenant:")
        print("   1. Vous connecter avec n'importe quel compte candidat")
        print("   2. Cliquer sur 'Analyser GitHub' dans le profil")
        print("   3. Voir les résultats de l'analyse GitHub")
        
        print("\n📊 Comptes configurés:")
        print("   • candidat@test.com    -> GitHub: tj (Express.js creator)")
        print("   • aghribazar@gmail.com -> GitHub: torvalds (Linux creator)")
        print("   • oussama@gmail.com    -> GitHub: gvanrossum (Python creator)")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_all_github_usernames()
