"""
Script de test pour l'envoi d'emails
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.email_service import email_service

def test_email():
    print("🧪 Test du service d'envoi d'emails\n")
    print("=" * 70)
    
    # Vérifier la configuration
    print("\n📋 Configuration actuelle:")
    print(f"   SMTP Host: {email_service.smtp_host}")
    print(f"   SMTP Port: {email_service.smtp_port}")
    print(f"   SMTP User: {email_service.smtp_user or '❌ Non configuré'}")
    print(f"   From Email: {email_service.from_email or '❌ Non configuré'}")
    print(f"   From Name: {email_service.from_name}")
    
    if not email_service.smtp_user or not email_service.smtp_password:
        print("\n" + "=" * 70)
        print("\n⚠️  CONFIGURATION EMAIL MANQUANTE\n")
        print("Pour activer l'envoi d'emails, configurez les variables suivantes")
        print("dans le fichier .env du backend:\n")
        print("SMTP_HOST=smtp.gmail.com")
        print("SMTP_PORT=587")
        print("SMTP_USER=votre-email@gmail.com")
        print("SMTP_PASSWORD=votre-app-password")
        print("FROM_EMAIL=votre-email@gmail.com")
        print("FROM_NAME=SmartRecruitMe")
        print("\n📝 Pour Gmail:")
        print("   1. Allez sur: https://myaccount.google.com/apppasswords")
        print("   2. Créez un 'App Password' pour 'Mail'")
        print("   3. Utilisez ce mot de passe dans SMTP_PASSWORD")
        print("\n" + "=" * 70)
        return
    
    print("\n" + "=" * 70)
    print("\n🧪 Test d'envoi d'email de démonstration\n")
    
    # Email de test
    test_email_address = input("Entrez votre email pour recevoir un test (ou appuyez sur Entrée pour annuler): ").strip()
    
    if not test_email_address:
        print("\n❌ Test annulé")
        return
    
    print(f"\n📧 Envoi d'un email de test à {test_email_address}...")
    
    # Données de test
    success = email_service.send_new_job_notification(
        candidate_email=test_email_address,
        candidate_name="Candidat Test",
        job_title="Développeur Full Stack Senior",
        company_name="TechCorp Morocco",
        job_description="Nous recherchons un développeur Full Stack passionné pour rejoindre notre équipe. Vous travaillerez sur des projets innovants utilisant React, Node.js et Python.",
        required_skills=["React", "Node.js", "Python", "MongoDB", "Docker"],
        location="Casablanca, Maroc",
        contract_type="CDI"
    )
    
    if success:
        print("\n✅ Email envoyé avec succès!")
        print(f"   Vérifiez votre boîte de réception: {test_email_address}")
        print("   (Vérifiez aussi les spams si vous ne le voyez pas)")
    else:
        print("\n❌ Échec de l'envoi de l'email")
        print("   Vérifiez votre configuration SMTP dans le fichier .env")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    test_email()
