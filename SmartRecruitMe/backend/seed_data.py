"""
Script pour créer des données de test dans la base de données
Exécuter: python seed_data.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine, Base
from app.models import User, Candidate, Recruiter, JobOffer, UserRole
from app.auth import get_password_hash

def seed_database():
    # Créer les tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Vérifier si des données existent déjà
        existing_users = db.query(User).count()
        if existing_users > 0:
            print("⚠️  Des données existent déjà. Suppression...")
            db.query(User).delete()
            db.commit()
        
        print("🌱 Création des données de test...")
        
        # Créer un candidat de test
        candidate_user = User(
            email="candidat@test.com",
            hashed_password=get_password_hash("test123"),
            role=UserRole.CANDIDATE
        )
        db.add(candidate_user)
        db.commit()
        db.refresh(candidate_user)
        
        candidate = Candidate(
            user_id=candidate_user.id,
            full_name="Maroua Idomar",
            github_username="marouaidomar",
            location="Rabat, Maroc",
            phone="+212 6 12 34 56 78"
        )
        db.add(candidate)
        
        # Créer un recruteur de test
        recruiter_user = User(
            email="recruteur@test.com",
            hashed_password=get_password_hash("test123"),
            role=UserRole.RECRUITER
        )
        db.add(recruiter_user)
        db.commit()
        db.refresh(recruiter_user)
        
        recruiter = Recruiter(
            user_id=recruiter_user.id,
            company_name="TechCorp Morocco",
            full_name="Azar Aghrib",
            phone="+212 6 98 76 54 32"
        )
        db.add(recruiter)
        db.commit()
        db.refresh(recruiter)
        
        # Créer des offres d'emploi de test
        jobs = [
            {
                "title": "Développeur Full Stack",
                "description": "Nous recherchons un développeur Full Stack passionné pour rejoindre notre équipe. Vous travaillerez sur des projets innovants utilisant React, Node.js et Python.",
                "required_skills": ["React", "Node.js", "Python", "MongoDB", "Docker"],
                "experience_required": 2,
                "location": "Casablanca, Maroc",
                "salary_range": "25k-35k MAD",
                "contract_type": "CDI"
            },
            {
                "title": "Data Scientist",
                "description": "Rejoignez notre équipe data pour développer des modèles de machine learning et analyser de grandes quantités de données.",
                "required_skills": ["Python", "Machine Learning", "TensorFlow", "SQL", "Pandas"],
                "experience_required": 3,
                "location": "Rabat, Maroc",
                "salary_range": "30k-45k MAD",
                "contract_type": "CDI"
            },
            {
                "title": "DevOps Engineer",
                "description": "Nous cherchons un ingénieur DevOps pour automatiser nos processus de déploiement et gérer notre infrastructure cloud.",
                "required_skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux"],
                "experience_required": 2,
                "location": "Remote",
                "salary_range": "28k-40k MAD",
                "contract_type": "CDI"
            }
        ]
        
        for job_data in jobs:
            job = JobOffer(
                recruiter_id=recruiter.id,
                **job_data
            )
            db.add(job)
        
        db.commit()
        
        print("✅ Données de test créées avec succès!")
        print("\n📧 Comptes de test:")
        print("   Candidat: candidat@test.com / test123")
        print("   Recruteur: recruteur@test.com / test123")
        print("\n🚀 Vous pouvez maintenant vous connecter!")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
