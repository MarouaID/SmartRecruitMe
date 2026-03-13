"""
Script simple pour configurer le mot de passe Gmail
"""

print("=" * 70)
print("  📧 CONFIGURATION DU MOT DE PASSE GMAIL")
print("=" * 70)

print("\n1️⃣  Vous avez créé le App Password sur Google?")
print("2️⃣  Vous avez copié le mot de passe de 16 caractères?")
print()

app_password = input("Collez votre App Password ici (avec ou sans espaces): ").strip()

# Nettoyer le mot de passe (enlever les espaces)
app_password_clean = app_password.replace(" ", "")

if len(app_password_clean) != 16:
    print(f"\n⚠️  Le mot de passe doit faire 16 caractères!")
    print(f"   Vous avez entré: {len(app_password_clean)} caractères")
    print(f"   Exemple valide: abcdefghijklmnop")
    exit(1)

print(f"\n✅ Mot de passe valide: {app_password_clean[:4]}************")

# Mettre à jour le fichier .env
env_path = ".env"

try:
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    with open(env_path, 'w') as f:
        for line in lines:
            if line.startswith("SMTP_PASSWORD="):
                f.write(f"SMTP_PASSWORD={app_password_clean}\n")
                print("✅ SMTP_PASSWORD mis à jour dans .env")
            else:
                f.write(line)
    
    print("\n" + "=" * 70)
    print("\n🎉 CONFIGURATION TERMINÉE!\n")
    print("Maintenant testez l'envoi d'email:")
    print("   python3 test_email_simple.py")
    print("\n" + "=" * 70)

except Exception as e:
    print(f"\n❌ Erreur: {e}")
