"""
Script pour tester l'API GitHub et diagnostiquer le problème
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.github_agent import GitHubAgent
import requests

def test_github_api():
    print("🔍 Test de l'API GitHub...\n")
    
    # Test 1: Connexion directe à l'API
    print("=" * 70)
    print("TEST 1: Connexion directe à l'API GitHub")
    print("=" * 70)
    
    test_username = "torvalds"
    url = f"https://api.github.com/users/{test_username}"
    
    try:
        response = requests.get(url, timeout=10)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Rate Limit Remaining: {response.headers.get('X-RateLimit-Remaining', 'N/A')}")
        print(f"Rate Limit Reset: {response.headers.get('X-RateLimit-Reset', 'N/A')}")
        
        if response.status_code == 200:
            print("✅ API GitHub accessible")
            data = response.json()
            print(f"   User: {data.get('login')}")
            print(f"   Public Repos: {data.get('public_repos')}")
        elif response.status_code == 403:
            print("❌ Rate limit dépassé!")
            print("   Solution: Attendre ou configurer un token GitHub")
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(f"   Message: {response.text[:200]}")
    except Exception as e:
        print(f"❌ Exception: {e}")
    
    print("\n" + "=" * 70)
    print("TEST 2: Test avec GitHubAgent")
    print("=" * 70)
    
    agent = GitHubAgent()
    
    test_accounts = ["torvalds", "tj", "gvanrossum"]
    
    for username in test_accounts:
        print(f"\n📊 Test: {username}")
        try:
            result = agent.analyze(username)
            
            if result.get("status") == "done":
                print(f"   ✅ Succès!")
                print(f"   Score: {result.get('github_score', 0)}%")
                print(f"   Repos: {result.get('total_repos', 0)}")
                print(f"   Languages: {', '.join(result.get('top_languages', [])[:3])}")
            elif result.get("status") == "error":
                print(f"   ❌ Erreur: {result.get('message', 'Unknown')}")
            else:
                print(f"   ⚠️  Status: {result.get('status', 'Unknown')}")
        except Exception as e:
            print(f"   ❌ Exception: {str(e)[:100]}")
    
    print("\n" + "=" * 70)
    print("TEST 3: Vérification des candidats dans la DB")
    print("=" * 70)
    
    from app.database import SessionLocal
    from app.models import Candidate, User
    
    db = SessionLocal()
    
    try:
        candidates = db.query(Candidate).all()
        
        for candidate in candidates:
            user = db.query(User).filter(User.id == candidate.user_id).first()
            print(f"\n📋 {candidate.full_name}")
            print(f"   Email: {user.email if user else 'N/A'}")
            print(f"   GitHub: '{candidate.github_username}'")
            print(f"   GitHub (repr): {repr(candidate.github_username)}")
            
            if candidate.github_username:
                # Nettoyer les espaces
                clean_username = candidate.github_username.strip()
                if clean_username != candidate.github_username:
                    print(f"   ⚠️  Espaces détectés! Nettoyage...")
                    candidate.github_username = clean_username
                    db.commit()
                    print(f"   ✅ Nettoyé: '{clean_username}'")
    finally:
        db.close()
    
    print("\n" + "=" * 70)
    print("DIAGNOSTIC COMPLET")
    print("=" * 70)
    print("\n💡 Solutions possibles:")
    print("   1. Si rate limit dépassé: Attendre 1 heure ou configurer GITHUB_TOKEN")
    print("   2. Si problème réseau: Vérifier la connexion internet")
    print("   3. Si username invalide: Vérifier l'orthographe")
    print("   4. Redémarrer le backend après les corrections")

if __name__ == "__main__":
    test_github_api()
