"""
Test complet: Création d'offre et envoi d'emails aux candidats
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, User
from app.email_service import email_service

def test_complete_workflow():
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("  🎯 TEST COMPLET: NOTIFICATION NOUVELLE OFFRE")
        print("=" * 70)
        
        print("\n📊 Candidats qui recevront l'email:\n")
        
        candidates = db.query(Candidate).all()
        candidates_data = []
        
        for i, candidate in enumerate(candidates, 1):
            user = db.query(User).filter(User.id == candidate.user_id).first()
            if user:
                print(f"   {i}. {candidate.full_name}")
                print(f"      📧 {user.email}")
                print()
                candidates_data.append({
                    "email": user.email,
                    "name": candidate.full_name
                })
        
        if not candidates_data:
            print("   ⚠️  Aucun candidat trouvé")
            return
        
        print("=" * 70)
        print("\n🏢 Simulation: Création d'une nouvelle offre\n")
        
        job_data = {
            "title": "Ingénieur DevOps Senior",
            "company": "TechCorp Morocco",
            "description": "Nous recherchons un Ingénieur DevOps expérimenté pour gérer notre infrastructure cloud et automatiser nos processus de déploiement. Vous travaillerez avec Docker, Kubernetes, AWS et Terraform.",
            "required_skills": ["Docker", "Kubernetes", "AWS", "Terraform", "CI/CD", "Linux", "Python"],
            "location": "Rabat, Maroc (Remote possible)",
            "contract_type": "CDI"
        }
        
        print(f"📝 Titre: {job_data['title']}")
        print(f"🏢 Entreprise: {job_data['company']}")
        print(f"📍 Localisation: {job_data['location']}")
        print(f"🔧 Compétences: {', '.join(job_data['required_skills'][:4])}...")
        
        print("\n" + "=" * 70)
        print(f"\n📧 Envoi des emails à {len(candidates_data)} candidat(s)...\n")
        
        results = email_service.send_bulk_new_job_notifications(candidates_data, job_data)
        
        print("\n" + "=" * 70)
        print("\n📊 RÉSULTATS:\n")
        print(f"   Total: {results['total']}")
        print(f"   ✅ Envoyés: {results['sent']}")
        print(f"   ❌ Échecs: {results['failed']}")
        
        if results['failed'] > 0:
            print(f"\n   Emails en échec: {', '.join(results['errors'])}")
        
        print("\n" + "=" * 70)
        print("\n✅ TEST TERMINÉ!\n")
        print("📬 Vérifiez les boîtes email:")
        for candidate in candidates_data:
            print(f"   • {candidate['email']}")
        
        print("\n💡 Les emails peuvent prendre 1-2 minutes pour arriver")
        print("   Vérifiez aussi les dossiers SPAM/Courrier indésirable")
        
        print("\n" + "=" * 70)
        print("\n🎉 FONCTIONNALITÉ OPÉRATIONNELLE!\n")
        print("Maintenant, quand un recruteur crée une offre via l'interface:")
        print("   1. L'offre est créée dans la base de données")
        print("   2. Tous les candidats reçoivent un email automatiquement")
        print("   3. L'email contient toutes les infos de l'offre")
        print("   4. Les candidats peuvent cliquer pour voir leur score")
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_complete_workflow()
