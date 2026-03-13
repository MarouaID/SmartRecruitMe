"""
Guide pour configurer un token GitHub
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                    RATE LIMIT GITHUB DÉPASSÉ                         ║
╚══════════════════════════════════════════════════════════════════════╝

🔴 PROBLÈME: 
   L'API GitHub limite à 60 requêtes/heure sans authentification.
   Vous avez dépassé cette limite.

✅ SOLUTION 1: Attendre 1 heure
   Le rate limit se réinitialise automatiquement.

✅ SOLUTION 2: Configurer un token GitHub (RECOMMANDÉ)
   Avec un token: 5000 requêtes/heure

📝 ÉTAPES POUR CRÉER UN TOKEN GITHUB:

1. Allez sur: https://github.com/settings/tokens

2. Cliquez sur "Generate new token" > "Generate new token (classic)"

3. Donnez un nom: "SmartRecruitMe"

4. Sélectionnez les permissions:
   ✓ public_repo (ou repo si vous voulez accéder aux repos privés)
   ✓ read:user

5. Cliquez sur "Generate token"

6. COPIEZ le token (vous ne pourrez plus le voir après!)

7. Ajoutez-le dans le fichier .env du backend:
   
   GITHUB_TOKEN=ghp_votre_token_ici

8. Redémarrez le backend

═══════════════════════════════════════════════════════════════════════

🔧 SOLUTION TEMPORAIRE: Utiliser des données mockées

Si vous voulez tester sans attendre, je peux créer un mode "mock"
qui simule les données GitHub sans appeler l'API.

═══════════════════════════════════════════════════════════════════════
""")

# Vérifier quand le rate limit se réinitialise
import time
from datetime import datetime

reset_timestamp = 1773429192
reset_time = datetime.fromtimestamp(reset_timestamp)
now = datetime.now()
wait_time = (reset_time - now).total_seconds()

if wait_time > 0:
    hours = int(wait_time // 3600)
    minutes = int((wait_time % 3600) // 60)
    print(f"⏰ Le rate limit se réinitialise dans: {hours}h {minutes}min")
    print(f"   Heure de réinitialisation: {reset_time.strftime('%H:%M:%S')}")
else:
    print("✅ Le rate limit devrait être réinitialisé maintenant!")
    print("   Essayez de relancer l'analyse GitHub.")

print("\n" + "=" * 70)
