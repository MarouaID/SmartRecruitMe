# 📝 AIDE-MÉMOIRE - Commandes SmartRecruitMe

## 🚀 Démarrage

### Avec Docker (Recommandé)
```bash
# Démarrer tous les services
docker-compose up --build

# Démarrer en arrière-plan
docker-compose up -d

# Arrêter les services
docker-compose down

# Arrêter et supprimer les volumes (reset complet)
docker-compose down -v
```

### Sans Docker

#### Backend
```bash
cd SmartRecruitMe/backend

# Créer environnement virtuel
python -m venv venv

# Activer (Windows)
venv\Scripts\activate

# Activer (Linux/Mac)
source venv/bin/activate

# Installer dépendances
pip install -r requirements.txt

# Télécharger modèle spaCy
python -m spacy download en_core_web_md

# Démarrer serveur
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd SmartRecruitMe/frontend

# Installer dépendances
npm install

# Démarrer serveur de développement
npm start

# Build pour production
npm run build
```

## 🔧 Maintenance

### Docker
```bash
# Voir les logs
docker-compose logs

# Logs d'un service spécifique
docker-compose logs backend
docker-compose logs frontend

# Suivre les logs en temps réel
docker-compose logs -f

# Voir les services en cours
docker-compose ps

# Redémarrer un service
docker-compose restart backend

# Reconstruire un service
docker-compose up --build backend
```

### Base de données
```bash
# Se connecter à MySQL
docker-compose exec db mysql -u smartrecruit -p

# Créer les données de test
cd backend
python seed_data.py

# Migrations (si nécessaire)
cd backend
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Redis
```bash
# Se connecter à Redis
docker-compose exec redis redis-cli

# Vider le cache
docker-compose exec redis redis-cli FLUSHALL
```

## 🧪 Tests et Vérification

```bash
# Vérifier le système
cd backend
python check_system.py

# Tester l'API
curl http://localhost:8000/health

# Voir la documentation API
# Ouvrir http://localhost:8000/docs dans le navigateur
```

## 📦 Installation des dépendances

### Backend
```bash
# Installer une nouvelle dépendance
pip install nom-du-package

# Mettre à jour requirements.txt
pip freeze > requirements.txt
```

### Frontend
```bash
# Installer une nouvelle dépendance
npm install nom-du-package

# Installer en dev
npm install --save-dev nom-du-package
```

## 🐛 Dépannage

### Problème de port
```bash
# Trouver le processus utilisant le port 8000
netstat -ano | findstr :8000

# Tuer le processus (Windows)
taskkill /PID <PID> /F

# Tuer le processus (Linux/Mac)
kill -9 <PID>
```

### Problème Docker
```bash
# Nettoyer Docker
docker system prune -a

# Supprimer tous les conteneurs
docker rm -f $(docker ps -aq)

# Supprimer toutes les images
docker rmi -f $(docker images -q)

# Supprimer tous les volumes
docker volume rm $(docker volume ls -q)
```

### Problème npm
```bash
cd frontend

# Nettoyer le cache
npm cache clean --force

# Supprimer node_modules
rm -rf node_modules package-lock.json

# Réinstaller
npm install
```

### Problème Python
```bash
cd backend

# Supprimer le cache
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -rf {} +

# Réinstaller les dépendances
pip install --force-reinstall -r requirements.txt
```

## 📊 Monitoring

### Logs
```bash
# Backend logs
docker-compose logs -f backend

# Frontend logs
docker-compose logs -f frontend

# Database logs
docker-compose logs -f db

# Tous les logs
docker-compose logs -f
```

### Ressources
```bash
# Voir l'utilisation des ressources
docker stats

# Voir les processus
docker-compose top
```

## 🔐 Sécurité

### Générer une nouvelle clé secrète
```python
import secrets
print(secrets.token_urlsafe(32))
```

### Changer les mots de passe
```bash
# Éditer docker-compose.yml
# Changer MYSQL_PASSWORD et MYSQL_ROOT_PASSWORD

# Recréer les services
docker-compose down -v
docker-compose up --build
```

## 📝 Git

```bash
# Initialiser le repo
git init

# Ajouter tous les fichiers
git add .

# Commit
git commit -m "Initial commit - SmartRecruitMe"

# Ajouter remote
git remote add origin <url>

# Push
git push -u origin main
```

## 🚀 Déploiement

### Build production
```bash
# Backend
cd backend
docker build -t smartrecruitme-backend .

# Frontend
cd frontend
npm run build
docker build -t smartrecruitme-frontend .
```

### Variables d'environnement production
```bash
# Backend
export DATABASE_URL="mysql+pymysql://user:pass@host:3306/db"
export SECRET_KEY="production-secret-key"
export GITHUB_TOKEN="your-token"

# Frontend
export REACT_APP_API_URL="https://api.votre-domaine.com"
```

## 📞 URLs importantes

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- MySQL: localhost:3306
- Redis: localhost:6379

## 🎯 Comptes de test

- **Candidat**: candidat@test.com / test123
- **Recruteur**: recruteur@test.com / test123

## 💡 Astuces

### Développement rapide
```bash
# Terminal 1: Backend avec auto-reload
cd backend
uvicorn app.main:app --reload

# Terminal 2: Frontend avec hot-reload
cd frontend
npm start

# Terminal 3: Logs
docker-compose logs -f db redis
```

### Debug
```python
# Ajouter dans le code Python
import pdb; pdb.set_trace()

# Ou
import ipdb; ipdb.set_trace()
```

### Performance
```bash
# Vider le cache Redis
docker-compose exec redis redis-cli FLUSHALL

# Optimiser la base de données
docker-compose exec db mysql -u root -p -e "OPTIMIZE TABLE smartrecruitme.*"
```

---

**Gardez ce fichier à portée de main pendant le développement ! 📌**
