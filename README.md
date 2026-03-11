<<<<<<< HEAD
# 🚀 SmartRecruitMe - Plateforme Intelligente de Recrutement

## 📋 Description

SmartRecruitMe est une plateforme innovante qui transforme le recrutement en combinant l'analyse automatisée des CV et l'évaluation des projets GitHub pour fournir un profil complet et interactif des candidats.

## ✨ Fonctionnalités

### Pour les Candidats
- 📄 Upload et analyse automatique de CV (PDF/DOCX)
- 🔍 Analyse intelligente du profil GitHub
- 📊 Visualisation des compétences et scores
- 🎯 Matching automatique avec les offres d'emploi
- 💡 Recommandations personnalisées

### Pour les Recruteurs
- 📝 Création et gestion d'offres d'emploi
- 👥 Visualisation des candidats avec scores de matching
- 🎨 Dashboard interactif et moderne
- 🔎 Filtrage et recherche avancée
- 📈 Statistiques en temps réel

## 🛠️ Stack Technologique

### Backend
- **FastAPI** - Framework Python moderne et rapide
- **MySQL** - Base de données relationnelle
- **Redis** - Cache et gestion des tâches
- **SQLAlchemy** - ORM Python
- **spaCy** - Traitement du langage naturel
- **Scikit-learn** - Machine Learning pour le matching

### Frontend
- **React 18** - Bibliothèque UI
- **TypeScript** - Typage statique
- **Tailwind CSS** - Framework CSS moderne
- **Recharts** - Visualisations de données
- **Lucide React** - Icônes modernes
- **React Hot Toast** - Notifications élégantes

## 🚀 Installation et Démarrage

### Prérequis
- Docker et Docker Compose
- Node.js 18+ (pour développement local)
- Python 3.11+ (pour développement local)

### Méthode 1: Avec Docker (Recommandé)

```bash
# Cloner le projet
cd SmartRecruitMe

# Démarrer tous les services
docker-compose up --build

# Le backend sera disponible sur http://localhost:8000
# Le frontend sera disponible sur http://localhost:3000
# La documentation API sur http://localhost:8000/docs
```

### Méthode 2: Développement Local

#### Backend

```bash
cd backend

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Télécharger le modèle spaCy
python -m spacy download en_core_web_md

# Configurer les variables d'environnement
# Éditer le fichier .env avec vos configurations

# Démarrer le serveur
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend

```bash
cd frontend

# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm start
```

## 🔧 Configuration

### Backend (.env)
```env
DATABASE_URL=mysql+pymysql://smartrecruit:password@localhost:3306/smartrecruitme
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key-change-in-production
GITHUB_TOKEN=your-github-personal-access-token
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000
```

## 📊 Architecture

```
SmartRecruitMe/
├── backend/
│   ├── app/
│   │   ├── agents/          # Agents d'analyse (CV, GitHub, Matching)
│   │   ├── models/          # Modèles SQLAlchemy
│   │   ├── routes/          # Routes API
│   │   ├── schemas/         # Schémas Pydantic
│   │   ├── main.py          # Point d'entrée FastAPI
│   │   ├── orchestrator.py  # Orchestration des agents
│   │   └── auth.py          # Authentification JWT
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/      # Composants réutilisables
│   │   ├── pages/           # Pages de l'application
│   │   ├── services/        # Services API
│   │   ├── context/         # Contextes React
│   │   └── App.tsx          # Composant principal
│   └── package.json
└── docker-compose.yml
```

## 🎯 Utilisation

### Candidat

1. **S'inscrire** en tant que candidat
2. **Uploader votre CV** (PDF ou DOCX)
3. **Ajouter votre username GitHub** (optionnel)
4. **Visualiser votre profil** avec scores et compétences
5. **Consulter les offres compatibles** avec votre profil

### Recruteur

1. **S'inscrire** en tant que recruteur
2. **Créer une offre d'emploi** avec compétences requises
3. **Lancer le matching** pour trouver les meilleurs candidats
4. **Consulter les profils détaillés** des candidats
5. **Filtrer et trier** selon vos critères

## 🔐 Sécurité

- Authentification JWT avec tokens sécurisés
- Hachage des mots de passe avec bcrypt
- Validation des données avec Pydantic
- Protection CORS configurée
- Variables d'environnement pour les secrets

## 📈 Algorithmes de Matching

Le système utilise plusieurs algorithmes pour calculer le score de compatibilité:

1. **Analyse CV** (25%)
   - Extraction des compétences techniques
   - Détection de l'expérience
   - Analyse de la formation

2. **Analyse GitHub** (25%)
   - Diversité technologique
   - Régularité des contributions
   - Qualité des projets
   - Collaboration

3. **Matching Compétences** (35%)
   - Correspondance exacte des compétences
   - Similarité sémantique

4. **Expérience** (15%)
   - Années d'expérience vs requis

## 🎨 Design

Interface moderne avec:
- Gradients élégants
- Animations fluides
- Design responsive
- Dark mode ready
- Composants réutilisables

## 📝 API Documentation

La documentation interactive de l'API est disponible sur:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🤝 Équipe

- **Azar Aghrib**
- **Maroua Idomar**

ENSA GI4 - Projet SmartRecruitMe

## 📄 Licence

Ce projet est développé dans le cadre d'une compétition académique.

## 🚀 Déploiement

Pour déployer en production:

1. Modifier les variables d'environnement
2. Utiliser un serveur de production (Gunicorn/Nginx)
3. Configurer HTTPS
4. Utiliser une base de données production
5. Activer les logs et monitoring

## 💡 Améliorations Futures

- [ ] Support de plus de formats de CV
- [ ] Analyse GitLab en plus de GitHub
- [ ] Chat en temps réel recruteur-candidat
- [ ] Système de recommandations ML avancé
- [ ] Export PDF des profils
- [ ] Notifications par email
- [ ] Tests automatisés complets
- [ ] Internationalisation (i18n)

---

**Fait avec ❤️ par l'équipe ARIA**
=======
# SmartRecruitMe
>>>>>>> 6562f6a49ab9da87ca7d05fe3640783440ac5a41
