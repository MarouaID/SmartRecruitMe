"""
Test simple d'envoi d'email
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.email_service import EmailService

print("=" * 70)
print("  🧪 TEST D'ENVOI D'EMAIL")
print("=" * 70)

email_service = EmailService()

print(f"\n📋 Configuration:")
print(f"   SMTP: {email_service.smtp_host}:{email_service.smtp_port}")
print(f"   User: {email_service.smtp_user}")
print(f"   Password: {'✅ Configuré' if email_service.smtp_password else '❌ Manquant'}")

if not email_service.smtp_password:
    print("\n❌ Le mot de passe SMTP n'est pas configuré!")
    print("   Lancez: python3 configure_email.py")
    exit(1)

print("\n📧 Envoi d'un email de test à aghribazar@gmail.com...")

success = email_service.send_new_job_notification(
    candidate_email="aghribazar@gmail.com",
    candidate_name="Azar Aghrib",
    job_title="Développeur Full Stack - EMAIL DE TEST",
    company_name="SmartRecruitMe",
    job_description="Ceci est un email de test. Si vous recevez cet email, la configuration fonctionne parfaitement! 🎉",
    required_skills=["React", "Node.js", "Python", "MongoDB", "Docker"],
    location="Casablanca, Maroc",
    contract_type="CDI"
)

print("\n" + "=" * 70)

if success:
    print("\n✅ EMAIL ENVOYÉ AVEC SUCCÈS!\n")
    print("📬 Vérifiez votre boîte: aghribazar@gmail.com")
    print("   (Vérifiez aussi les SPAMS si vous ne le voyez pas)")
    print("\n💡 L'email peut prendre 1-2 minutes pour arriver")
else:
    print("\n❌ ÉCHEC DE L'ENVOI\n")
    print("Vérifiez:")
    print("   1. Le App Password est correct")
    print("   2. La validation en 2 étapes est activée sur Gmail")
    print("   3. Votre connexion internet")

print("\n" + "=" * 70)
