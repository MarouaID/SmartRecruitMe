"""
Script de démonstration de la fonctionnalité d'envoi d'emails
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Candidate, User, Recruiter
from app.email_service import email_service

def demo_email_notification():
    db = SessionLocal()
    
    try:
        print("=" * 70)
        print("  📧 DÉMONSTRATION: Notification Email Nouvelle Offre")
        print("=" * 70)
        
        # Vérifier la configuration
        if email_service.smtp_user and email_service.smtp_password:
            print("\n✅ Configuration SMTP détectée")
            print(f"   Les emails seront RÉELLEMENT envoyés depuis: {email_service.from_email}")
        else:
            print("\n⚠️  Mode DÉMONSTRATION activé")
            print("   Les emails seront simulés (pas d'envoi réel)")
            print("   Pour activer l'envoi réel, configurez SMTP dans .env")
        
        print("\n" + "=" * 70)
        print("\n📊 Candidats inscrits sur la plateforme:\n")
        
        # Récupérer tous les candidats
        candidates = db.query(Candidate).all()
        
        candidates_data = []
        for i, candidate in enumerate(candidates, 1):
            user = db.query(User).filter(User.id == candidate.user_id).first()
            if user:
                print(f"   {i}. {candidate.full_name}")
                print(f"      Email: {user.email}")
                print(f"      GitHub: {candidate.github_username or 'Non défini'}")
                print()
                
                candidates_data.append({
                    "email": user.email,
                    "name": candidate.full_name
                })
        
        if not candidates_data:
            print("   ⚠️  Aucun candidat trouvé")
            return
        
        print("=" * 70)
        print("\n🏢 Simulation: Un recruteur crée une nouvelle offre\n")
        
        # Données de l'offre simulée
        job_data = {
            "title": "Développeur Full Stack Senior",
            "company": "TechCorp Morocco",
            "description": "Nous recherchons un développeur Full Stack passionné pour rejoindre notre équipe dynamique. Vous travaillerez sur des projets innovants utilisant les dernières technologies (React, Node.js, Python) et contribuerez à la création de solutions impactantes pour nos clients.",
            "required_skills": ["React", "Node.js", "Python", "MongoDB", "Docker", "TypeScript", "Git"],
            "location": "Casablanca, Maroc (Hybride)",
            "contract_type": "CDI"
        }
        
        print(f"📝 Offre: {job_data['title']}")
        print(f"🏢 Entreprise: {job_data['company']}")
        print(f"📍 Localisation: {job_data['location']}")
        print(f"🔧 Compétences: {', '.join(job_data['required_skills'][:5])}...")
        
        print("\n" + "=" * 70)
        print(f"\n📧 Envoi des notifications à {len(candidates_data)} candidat(s)...\n")
        
        # Envoyer les notifications
        results = email_service.send_bulk_new_job_notifications(candidates_data, job_data)
        
        print("\n" + "=" * 70)
        print("\n📊 RÉSULTATS:\n")
        print(f"   Total de candidats: {results['total']}")
        print(f"   ✅ Emails envoyés: {results['sent']}")
        print(f"   ❌ Échecs: {results['failed']}")
        
        if results['failed'] > 0:
            print(f"\n   Emails en échec: {', '.join(results['errors'])}")
        
        print("\n" + "=" * 70)
        
        if email_service.smtp_user and email_service.smtp_password:
            print("\n✅ Les emails ont été envoyés!")
            print("   Vérifiez les boîtes de réception des candidats")
            print("   (Vérifiez aussi les dossiers spam)")
        else:
            print("\n💡 Pour activer l'envoi réel d'emails:")
            print("   1. Consultez le fichier EMAIL_SETUP.md")
            print("   2. Configurez les variables SMTP dans .env")
            print("   3. Relancez ce script ou créez une offre via l'interface")
        
        print("\n" + "=" * 70)
        print("\n🎯 FONCTIONNEMENT EN PRODUCTION:\n")
        print("   1. Un recruteur se connecte sur la plateforme")
        print("   2. Il crée une nouvelle offre d'emploi")
        print("   3. L'offre est enregistrée dans la base de données")
        print("   4. Automatiquement, tous les candidats reçoivent un email")
        print("   5. L'email contient toutes les infos de l'offre")
        print("   6. Les candidats peuvent cliquer pour voir leur score de matching")
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    demo_email_notification()
