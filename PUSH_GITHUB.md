# 🚀 Guide pour Pousser vers GitHub

## ✅ Étape 1: Créer un dépôt sur GitHub

1. Aller sur https://github.com
2. Cliquer sur le bouton **"New"** ou **"+"** en haut à droite
3. Nommer le dépôt: **SmartRecruitMe**
4. Choisir **Public** ou **Private**
5. **NE PAS** cocher "Initialize with README"
6. Cliquer sur **"Create repository"**

## ✅ Étape 2: Lier votre dépôt local à GitHub

Copier l'URL de votre dépôt GitHub (elle ressemble à):
```
https://github.com/votre-username/SmartRecruitMe.git
```

Puis exécuter dans le terminal:

```bash
cd c:\Users\PC\Desktop\SmartRecruitMe

# Ajouter le remote
git remote add origin https://github.com/VOTRE-USERNAME/SmartRecruitMe.git

# Vérifier que le remote est ajouté
git remote -v
```

## ✅ Étape 3: Pousser vers GitHub

```bash
# Pousser vers la branche main
git push -u origin main
```

Si vous avez une erreur d'authentification, GitHub vous demandera de vous connecter.

## 🔐 Authentification GitHub

### Option 1: HTTPS (Recommandé)
GitHub vous demandera vos identifiants. Utilisez un **Personal Access Token** au lieu du mot de passe:

1. Aller sur GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Cliquer sur "Generate new token (classic)"
3. Cocher les permissions: `repo`, `workflow`
4. Copier le token généré
5. Utiliser ce token comme mot de passe lors du push

### Option 2: SSH
```bash
# Générer une clé SSH
ssh-keygen -t ed25519 -C "votre-email@example.com"

# Copier la clé publique
cat ~/.ssh/id_ed25519.pub

# Ajouter la clé sur GitHub → Settings → SSH and GPG keys → New SSH key

# Changer l'URL du remote
git remote set-url origin git@github.com:VOTRE-USERNAME/SmartRecruitMe.git

# Pousser
git push -u origin main
```

## 📝 Commandes Git Utiles

```bash
# Voir le statut
git status

# Voir l'historique
git log --oneline

# Ajouter des fichiers
git add .

# Créer un commit
git commit -m "Votre message"

# Pousser les changements
git push

# Tirer les changements
git pull

# Voir les remotes
git remote -v

# Créer une nouvelle branche
git checkout -b nom-de-branche

# Changer de branche
git checkout main
```

## 🎯 Après le Push

Votre projet sera visible sur:
```
https://github.com/VOTRE-USERNAME/SmartRecruitMe
```

## 📋 Checklist

- [ ] Dépôt créé sur GitHub
- [ ] Remote ajouté localement
- [ ] Premier push effectué
- [ ] Vérifier que tous les fichiers sont sur GitHub
- [ ] Ajouter une description au dépôt
- [ ] Ajouter des topics (tags): `react`, `fastapi`, `recruitment`, `ai`, `python`, `typescript`

## 🎨 Personnaliser le README sur GitHub

Le fichier README.md sera automatiquement affiché sur la page d'accueil de votre dépôt.

## 🔄 Pour les Mises à Jour Futures

```bash
# Après avoir modifié des fichiers
git add .
git commit -m "Description des changements"
git push
```

## 🤝 Collaborer avec votre Équipe

```bash
# Ajouter un collaborateur sur GitHub:
# Settings → Collaborators → Add people

# Cloner le projet (pour les collaborateurs)
git clone https://github.com/VOTRE-USERNAME/SmartRecruitMe.git

# Avant de travailler, toujours pull
git pull

# Après avoir travaillé
git add .
git commit -m "Message"
git push
```

## 🎉 C'est Fait !

Votre projet SmartRecruitMe est maintenant sur GitHub et prêt à être partagé ! 🚀

---

**Besoin d'aide ?**
- Documentation Git: https://git-scm.com/doc
- Documentation GitHub: https://docs.github.com
