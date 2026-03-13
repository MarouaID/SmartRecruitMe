"""
Script pour tester des comptes GitHub et trouver un avec un score d'environ 50%
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.github_agent import GitHubAgent

def test_github_accounts():
    agent = GitHubAgent()
    
    # Liste de comptes GitHub publics à tester
    test_accounts = [
        "torvalds",      # Linus Torvalds - probablement très haut
        "gvanrossum",    # Guido van Rossum - probablement haut
        "tj",            # TJ Holowaychuk - probablement haut
        "sindresorhus",  # Sindre Sorhus - probablement très haut
        "defunkt",       # Chris Wanstrath (GitHub co-founder)
        "mojombo",       # Tom Preston-Werner
        "pjhyett",       # PJ Hyett
        "wycats",        # Yehuda Katz
        "dhh",           # David Heinemeier Hansson
        "addyosmani",    # Addy Osmani
        "paulirish",     # Paul Irish
        "mdo",           # Mark Otto (Bootstrap)
        "fat",           # Jacob Thornton
        "jeresig",       # John Resig (jQuery)
        "isaacs",        # Isaac Schlueter (npm)
        "substack",      # James Halliday
        "rauchg",        # Guillermo Rauch
        "ry",            # Ryan Dahl (Node.js creator)
        "fabpot",        # Fabien Potencier (Symfony)
        "taylorotwell",  # Taylor Otwell (Laravel)
    ]
    
    print("🔍 Test de comptes GitHub pour trouver un score ~50%\n")
    print("=" * 70)
    
    results = []
    
    for username in test_accounts:
        try:
            print(f"\n📊 Test: {username}")
            result = agent.analyze(username)
            
            if result.get("status") == "done":
                score = result.get("github_score", 0)
                print(f"   Score: {score}%")
                print(f"   Repos: {result.get('total_repos', 0)}")
                print(f"   Languages: {', '.join(result.get('top_languages', [])[:3])}")
                print(f"   Régularité: {result.get('regularity_score', 0)}")
                print(f"   Collaboration: {result.get('collaboration_score', 0)}")
                print(f"   Qualité: {result.get('project_quality_score', 0)}")
                
                results.append({
                    "username": username,
                    "score": score,
                    "result": result
                })
            else:
                print(f"   ❌ Erreur: {result.get('message', 'Unknown error')}")
        
        except Exception as e:
            print(f"   ❌ Exception: {e}")
    
    print("\n" + "=" * 70)
    print("\n📈 Résultats triés par score:\n")
    
    results.sort(key=lambda x: x["score"])
    
    for r in results:
        print(f"{r['username']:20} - {r['score']:5.1f}%")
    
    # Trouver le plus proche de 50%
    print("\n" + "=" * 70)
    print("\n🎯 Comptes les plus proches de 50%:\n")
    
    closest = sorted(results, key=lambda x: abs(x["score"] - 50))[:5]
    
    for r in closest:
        diff = abs(r["score"] - 50)
        print(f"✓ {r['username']:20} - {r['score']:5.1f}% (diff: {diff:.1f}%)")
        print(f"  Repos: {r['result'].get('total_repos', 0)}")
        print(f"  Languages: {', '.join(r['result'].get('top_languages', []))}")
        print()
    
    if closest:
        best = closest[0]
        print("=" * 70)
        print(f"\n🏆 MEILLEUR CHOIX: {best['username']}")
        print(f"   Score: {best['score']}%")
        print(f"   Différence avec 50%: {abs(best['score'] - 50):.1f}%")
        print(f"\n   Utilisez ce compte pour tester!")

if __name__ == "__main__":
    test_github_accounts()
