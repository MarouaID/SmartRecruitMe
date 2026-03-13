import requests
from typing import Dict, List
from datetime import datetime, timedelta
from collections import Counter
import json

class GitHubAgent:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {}
        # Redis est optionnel maintenant
        self.redis_client = None
    
    def get_user_repos(self, username: str) -> List[Dict]:
        url = f"{self.base_url}/users/{username}/repos"
        params = {"per_page": 100, "sort": "updated"}
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching repos: {e}")
        
        return []
    
    def get_repo_languages(self, username: str, repo_name: str) -> Dict:
        url = f"{self.base_url}/repos/{username}/{repo_name}/languages"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching languages: {e}")
        
        return {}
    
    def get_user_events(self, username: str) -> List[Dict]:
        url = f"{self.base_url}/users/{username}/events"
        params = {"per_page": 100}
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching events: {e}")
        
        return []
    
    def calculate_language_diversity(self, repos: List[Dict], username: str) -> Dict:
        all_languages = []
        
        for repo in repos[:20]:
            if not repo.get('fork', False):
                languages = self.get_repo_languages(username, repo['name'])
                all_languages.extend(languages.keys())
        
        if not all_languages:
            return {"languages": [], "diversity_score": 0.0}
        
        language_counts = Counter(all_languages)
        top_languages = [lang for lang, _ in language_counts.most_common(5)]
        diversity_score = min(len(set(all_languages)) / 10.0, 1.0)
        
        return {
            "languages": top_languages,
            "diversity_score": diversity_score
        }
    
    def calculate_regularity(self, events: List[Dict]) -> float:
        if not events:
            return 0.0
        
        commit_events = [e for e in events if e['type'] in ['PushEvent', 'PullRequestEvent']]
        
        if len(commit_events) < 5:
            return 0.3
        
        dates = []
        for event in commit_events[:50]:
            try:
                date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                dates.append(date)
            except:
                continue
        
        if len(dates) < 2:
            return 0.3
        
        dates.sort()
        date_range = (dates[-1] - dates[0]).days
        
        if date_range == 0:
            return 0.5
        
        activity_rate = len(dates) / max(date_range, 1)
        regularity_score = min(activity_rate * 10, 1.0)
        
        return round(regularity_score, 2)
    
    def calculate_collaboration(self, repos: List[Dict], events: List[Dict]) -> float:
        collaboration_indicators = 0
        
        pr_events = [e for e in events if e['type'] == 'PullRequestEvent']
        collaboration_indicators += min(len(pr_events) / 10, 1.0) * 0.4
        
        issue_events = [e for e in events if e['type'] == 'IssuesEvent']
        collaboration_indicators += min(len(issue_events) / 10, 1.0) * 0.3
        
        forked_repos = [r for r in repos if r.get('fork', False)]
        collaboration_indicators += min(len(forked_repos) / 5, 1.0) * 0.3
        
        return round(collaboration_indicators, 2)
    
    def calculate_project_quality(self, repos: List[Dict]) -> float:
        if not repos:
            return 0.0
        
        quality_score = 0.0
        evaluated_repos = 0
        
        for repo in repos[:10]:
            if repo.get('fork', False):
                continue
            
            repo_score = 0.0
            
            if repo.get('description'):
                repo_score += 0.2
            
            if repo.get('stargazers_count', 0) > 0:
                repo_score += min(repo['stargazers_count'] / 10, 0.3)
            
            if repo.get('has_wiki') or repo.get('has_pages'):
                repo_score += 0.2
            
            if repo.get('size', 0) > 100:
                repo_score += 0.3
            
            quality_score += min(repo_score, 1.0)
            evaluated_repos += 1
        
        if evaluated_repos == 0:
            return 0.0
        
        return round(quality_score / evaluated_repos, 2)
    
    def infer_soft_skills(self, regularity: float, collaboration: float, quality: float) -> List[str]:
        soft_skills = []
        
        if regularity > 0.7:
            soft_skills.extend(["Régularité", "Discipline", "Persévérance"])
        elif regularity > 0.4:
            soft_skills.append("Régularité")
        
        if collaboration > 0.6:
            soft_skills.extend(["Travail en équipe", "Communication"])
        elif collaboration > 0.3:
            soft_skills.append("Collaboration")
        
        if quality > 0.7:
            soft_skills.extend(["Attention aux détails", "Professionnalisme"])
        elif quality > 0.4:
            soft_skills.append("Qualité du code")
        
        return list(set(soft_skills))
    
    def calculate_github_score(self, diversity: float, regularity: float, 
                               collaboration: float, quality: float) -> float:
        score = (
            diversity * 25 +
            regularity * 30 +
            collaboration * 20 +
            quality * 25
        )
        return round(score, 2)
    
    def analyze(self, username: str) -> Dict:
        if not username:
            return {
                "agent": "GITHUB_AGENT",
                "status": "error",
                "message": "No GitHub username provided"
            }
        
        repos = self.get_user_repos(username)
        
        if not repos:
            return {
                "agent": "GITHUB_AGENT",
                "status": "error",
                "message": "Could not fetch GitHub data or user has no repos"
            }
        
        events = self.get_user_events(username)
        
        language_data = self.calculate_language_diversity(repos, username)
        regularity = self.calculate_regularity(events)
        collaboration = self.calculate_collaboration(repos, events)
        quality = self.calculate_project_quality(repos)
        
        soft_skills = self.infer_soft_skills(regularity, collaboration, quality)
        github_score = self.calculate_github_score(
            language_data['diversity_score'],
            regularity,
            collaboration,
            quality
        )
        
        return {
            "agent": "GITHUB_AGENT",
            "status": "done",
            "top_languages": language_data['languages'],
            "total_repos": len(repos),
            "total_commits": len([e for e in events if e['type'] == 'PushEvent']),
            "regularity_score": regularity,
            "collaboration_score": collaboration,
            "project_quality_score": quality,
            "inferred_softskills": soft_skills,
            "github_score": github_score
        }
