# 🚀 DÉMARRAGE RAPIDE SANS DOCKER

## ⚡ MÉTHODE AUTOMATIQUE (LA PLUS SIMPLE)

Double-cliquez sur le fichier:
```
start-local.bat
```

C'est tout ! L'application va démarrer automatiquement.

---

## 📝 MÉTHODE MANUELLE

### Prérequis
- Python 3.11+ installé
- Node.js 18+ installé

### Terminal 1: Backend

```bash
# 1. Aller dans backend
cd c:\Users\PC\Desktop\SmartRecruitMe\SmartRecruitMe\backend

# 2. Créer environnement virtuel
python -m venv venv

# 3. Activer
venv\Scripts\activate

# 4. Installer dépendances (2-3 minutes)
pip install -r requirements.txt

# 5. Télécharger spaCy (1-2 minutes)
python -m spacy download en_core_web_md

# 6. Créer données de test
python seed_data.py

# 7. Démarrer backend
uvicorn app.main:app --reload
```

### Terminal 2: Frontend

```bash
# 1. Aller dans frontend
cd c:\Users\PC\Desktop\SmartRecruitMe\SmartRecruitMe\frontend

# 2. Installer dépendances (2-3 minutes)
npm install

# 3. Démarrer frontend
npm start
```

---

## 🌐 Accéder à l'application

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 👤 Comptes de test

- **Candidat**: candidat@test.com / test123
- **Recruteur**: recruteur@test.com / test123

---

## ⚠️ Notes importantes

1. **SQLite au lieu de MySQL**: L'app utilise SQLite (fichier local) au lieu de MySQL
2. **Pas de Redis**: Le cache est désactivé, tout fonctionne quand même
3. **Données locales**: Tout est stocké dans `smartrecruitme.db`

---

## 🐛 Problèmes courants

### Port 8000 déjà utilisé
```bash
# Trouver le processus
netstat -ano | findstr :8000

# Tuer le processus
taskkill /PID <PID> /F
```

### Erreur spaCy
```bash
python -m spacy download en_core_web_md
```

### Erreur npm
```bash
cd frontend
rm -rf node_modules
npm install
```

---

## 🎯 C'est prêt !

Ouvrez http://localhost:3000 et profitez ! 🚀
