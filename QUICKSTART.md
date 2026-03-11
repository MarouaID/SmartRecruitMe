# 🚀 DÉMARRAGE RAPIDE - SmartRecruitMe

## Option 1: Docker (Le plus simple)

```bash
# Dans le dossier SmartRecruitMe
cd SmartRecruitMe

# Démarrer tous les services
docker-compose up --build

# Attendre que tout démarre (2-3 minutes)
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

## Option 2: Sans Docker

### 1. Backend

```bash
cd SmartRecruitMe/backend

# Installer les dépendances
pip install -r requirements.txt
python -m spacy download en_core_web_md

# Démarrer MySQL et Redis localement
# Puis démarrer le backend
uvicorn app.main:app --reload
```

### 2. Frontend

```bash
cd SmartRecruitMe/frontend

# Installer les dépendances
npm install

# Démarrer le frontend
npm start
```

## 🎯 Premiers pas

1. Ouvrir http://localhost:3000
2. Cliquer sur "S'inscrire"
3. Créer un compte Candidat ou Recruteur
4. Profiter de la plateforme !

## 🔑 Comptes de test

### Candidat
- Email: candidat@test.com
- Password: test123

### Recruteur
- Email: recruteur@test.com
- Password: test123

## 📝 Notes importantes

- Le backend doit être démarré AVANT le frontend
- MySQL doit tourner sur le port 3306
- Redis doit tourner sur le port 6379
- Pour GitHub, ajoutez votre token dans backend/.env

## 🐛 Problèmes courants

### Port déjà utilisé
```bash
# Changer le port dans docker-compose.yml
ports:
  - "8001:8000"  # Au lieu de 8000:8000
```

### Base de données non accessible
```bash
# Vérifier que MySQL tourne
docker-compose ps

# Recréer la base
docker-compose down -v
docker-compose up --build
```

### Erreur npm
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## 📞 Support

En cas de problème, vérifier:
1. Les logs Docker: `docker-compose logs`
2. La connexion MySQL
3. Les variables d'environnement dans .env
