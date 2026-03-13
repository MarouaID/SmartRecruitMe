"""
Guide interactif pour configurer Gmail et tester l'envoi d'emails
"""
import sys
import os

def setup_gmail():
    print("=" * 70)
    print("  📧 CONFIGURATION GMAIL POUR SMARTRECRUITME")
    print("=" * 70)
    
    print("\n🔐 ÉTAPE 1: Créer un App Password Gmail\n")
    print("1. Ouvrez ce lien dans votre navigateur:")
    print("   👉 https://myaccount.google.com/apppasswords")
    print()
    print("2. Connectez-vous avec votre compte Gmail (aghribazar@gmail.com)")
    print()
    print("3. Si vous voyez 'App passwords', continuez.")
    print("   Si vous voyez un message d'erreur:")
    print("   - Activez la validation en 2 étapes d'abord")
    print("   - Allez sur: https://myaccount.google.com/security")
    print("   - Activez '2-Step Verification'")
    print("   - Puis retournez sur le lien des App passwords")
    print()
    print("4. Dans 'Select app', choisissez 'Mail'")
    print("5. Dans 'Select device', choisissez 'Other' et tapez 'SmartRecruitMe'")
    print("6. Cliquez sur 'Generate'")
    print()
    print("7. Vous verrez un mot de passe de 16 caractères comme:")
    print("   xxxx xxxx xxxx xxxx")
    print()
    
    print("=" * 70)
    input("\n⏸️  Appuyez sur Entrée quand vous avez généré le App Password...")
    
    print("\n🔐 ÉTAPE 2: Entrer le App Password\n")
    app_password = input("Collez votre App Password (16 caractères): ").strip().replace(" ", "")
    
    if len(app_password) != 16:
        print("\n⚠️  Le App Password doit faire 16 caractères!")
        print("   Exemple: abcdabcdabcdabcd")
        return
    
    print("\n📝 ÉTAPE 3: Mise à jour du fichier .env\n")
    
    # Lire le fichier .env
    env_path = "/Users/mac/Documents/RR/SmartRecruitMe/SmartRecruitMe/backend/.env"
    
    try:
        with open(env_path, 'r') as f:
            content = f.read()
        
        # Remplacer SMTP_PASSWORD
        if "SMTP_PASSWORD=" in content:
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                if line.startswith("SMTP_PASSWORD="):
                    new_lines.append(f"SMTP_PASSWORD={app_password}")
                else:
                    new_lines.append(line)
            
            new_content = '\n'.join(new_lines)
            
            with open(env_path, 'w') as f:
                f.write(new_content)
            
            print("✅ Fichier .env mis à jour!")
        else:
            print("⚠️  SMTP_PASSWORD non trouvé dans .env")
    
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return
    
    print("\n🧪 ÉTAPE 4: Test de l'envoi d'email\n")
    
    test_email = input("Entrez votre email pour recevoir un test (aghribazar@gmail.com): ").strip()
    
    if not test_email:
        test_email = "aghribazar@gmail.com"
    
    print(f"\n📧 Envoi d'un email de test à {test_email}...")
    
    # Importer et tester
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        from app.email_service import EmailService
        
        # Recharger le service avec la nouvelle config
        email_service = EmailService()
        
        success = email_service.send_new_job_notification(
            candidate_email=test_email,
            candidate_name="Azar Aghrib",
            job_title="Développeur Full Stack Senior - TEST",
            company_name="SmartRecruitMe",
            job_description="Ceci est un email de test pour vérifier que la configuration fonctionne correctement. Si vous recevez cet email, tout est OK!",
            required_skills=["React", "Node.js", "Python", "MongoDB", "Docker"],
            location="Casablanca, Maroc",
            contract_type="CDI"
        )
        
        if success:
            print("\n" + "=" * 70)
            print("\n✅ EMAIL ENVOYÉ AVEC SUCCÈS!\n")
            print(f"📬 Vérifiez votre boîte de réception: {test_email}")
            print("   (Vérifiez aussi le dossier SPAM/Courrier indésirable)")
            print("\n💡 Si vous ne voyez pas l'email:")
            print("   1. Attendez 1-2 minutes")
            print("   2. Vérifiez les spams")
            print("   3. Vérifiez que l'email est correct")
            print("\n" + "=" * 70)
            
            print("\n🎉 CONFIGURATION TERMINÉE!\n")
            print("Maintenant, quand un recruteur crée une offre:")
            print("✅ Tous les candidats recevront un email automatiquement")
            print("✅ L'email sera envoyé depuis: aghribazar@gmail.com")
            print("✅ Les logs apparaîtront dans la console du backend")
            
        else:
            print("\n❌ Échec de l'envoi")
            print("Vérifiez:")
            print("1. Le App Password est correct")
            print("2. La validation en 2 étapes est activée")
            print("3. Votre connexion internet")
    
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    setup_gmail()
