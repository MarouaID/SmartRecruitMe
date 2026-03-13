"""
Script pour tester plus de comptes GitHub
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.github_agent import GitHubAgent

def test_more_accounts():
    agent = GitHubAgent()
    
    # Comptes avec activité moyenne
    test_accounts = [
        "tj",              # 55.2% déjà testé
        "kennethreitz",    # Requests library
        "jashkenas",       # Backbone.js
        "mbostock",        # D3.js
        "yyx990803",       # Vue.js creator
        "gaearon",         # React core team
        "sebmarkbage",     # React core team
        "zpao",            # React core team
        "acdlite",         # React core team
        "bvaughn",         # React core team
        "sophiebits",      # React core team
        "trueadm",         # React core team
        "rickhanlonii",    # React core team
        "kassens",         # React core team
        "lunaruan",        # React core team
    ]
    
    print("🔍 Test de comptes GitHub supplémentaires\n")
    
    results = []
    
    for username in test_accounts:
        try:
            print(f"📊 {username:20}", end=" ")
            result = agent.analyze(username)
            
            if result.get("status") == "done":
                score = result.get("github_score", 0)
                print(f"- {score:5.1f}%")
                results.append({"username": username, "score": score, "result": result})
            else:
                print(f"- ❌ Erreur")
        except Exception as e:
            print(f"- ❌ Exception")
    
    print("\n" + "=" * 70)
    print("\n🎯 Comptes entre 40% et 60%:\n")
    
    in_range = [r for r in results if 40 <= r["score"] <= 60]
    in_range.sort(key=lambda x: abs(x["score"] - 50))
    
    for r in in_range:
        diff = abs(r["score"] - 50)
        print(f"✓ {r['username']:20} - {r['score']:5.1f}% (diff: {diff:.1f}%)")
    
    if in_range:
        best = in_range[0]
        print("\n" + "=" * 70)
        print(f"\n🏆 MEILLEUR CHOIX: {best['username']}")
        print(f"   Score GitHub: {best['score']}%")
        print(f"   Repos: {best['result'].get('total_repos', 0)}")
        print(f"   Languages: {', '.join(best['result'].get('top_languages', []))}")
        print(f"   Régularité: {best['result'].get('regularity_score', 0)}")
        print(f"   Collaboration: {best['result'].get('collaboration_score', 0)}")
        print(f"   Qualité: {best['result'].get('project_quality_score', 0)}")

if __name__ == "__main__":
    test_more_accounts()
