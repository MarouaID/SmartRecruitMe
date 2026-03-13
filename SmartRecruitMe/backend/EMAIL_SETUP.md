# 📧 Guide de Configuration des Emails - SmartRecruitMe

## 🎯 Fonctionnalité

Lorsqu'un recruteur crée une nouvelle offre d'emploi, tous les candidats inscrits sur la plateforme reçoivent automatiquement un email de notification avec:
- Le titre du poste
- Le nom de l'entreprise
- La description du poste
- Les compétences requises
- La localisation et le type de contrat
- Un lien direct vers la plateforme

## 📋 Configuration

### Option 1: Gmail (Recommandé pour les tests)

1. **Créer un App Password Gmail:**
   - Allez sur: https://myaccount.google.com/apppasswords
   - Connectez-vous avec votre compte Gmail
   - Sélectionnez "Mail" comme application
   - Sélectionnez "Other" comme appareil et nommez-le "SmartRecruitMe"
   - Cliquez sur "Generate"
   - Copiez le mot de passe généré (16 caractères)

2. **Configurer le fichier .env:**
   ```env
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=votre-email@gmail.com
   SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # App Password généré
   FROM_EMAIL=votre-email@gmail.com
   FROM_NAME=SmartRecruitMe
   ```

### Option 2: Outlook/Hotmail

```env
SMTP_HOST=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USER=votre-email@outlook.com
SMTP_PASSWORD=votre-mot-de-passe
FROM_EMAIL=votre-email@outlook.com
FROM_NAME=SmartRecruitMe
```

### Option 3: Yahoo Mail

```env
SMTP_HOST=smtp.mail.yahoo.com
SMTP_PORT=587
SMTP_USER=votre-email@yahoo.com
SMTP_PASSWORD=votre-app-password
FROM_EMAIL=votre-email@yahoo.com
FROM_NAME=SmartRecruitMe
```

### Option 4: SendGrid (Pour production)

```env
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASSWORD=votre-api-key-sendgrid
FROM_EMAIL=noreply@votredomaine.com
FROM_NAME=SmartRecruitMe
```

## 🧪 Test de la Configuration

1. **Installer les dépendances:**
   ```bash
   cd backend
   pip install aiosmtplib email-validator
   ```

2. **Tester l'envoi d'email:**
   ```bash
   python3 test_email.py
   ```

3. **Créer une offre via l'interface:**
   - Connectez-vous en tant que recruteur
   - Créez une nouvelle offre d'emploi
   - Les emails seront envoyés automatiquement en arrière-plan

## 📊 Vérification des Logs

Les logs d'envoi d'emails apparaissent dans la console du backend:
```
📧 Emails envoyés: 3/3
✅ Email envoyé à candidat@test.com
✅ Email envoyé à aghribazar@gmail.com
✅ Email envoyé à oussama@gmail.com
```

## 🎨 Aperçu de l'Email

L'email envoyé contient:
- **Header coloré** avec gradient violet
- **Carte de l'offre** avec toutes les informations
- **Tags de compétences** stylisés
- **Bouton CTA** pour voir l'offre complète
- **Design responsive** compatible mobile

## 🔧 Mode Démonstration (Sans Configuration Email)

Si vous ne configurez pas les emails, l'application fonctionne normalement mais:
- Les emails ne sont pas envoyés
- Les logs indiquent "Email non configuré"
- Aucune erreur n'est levée
- L'offre est créée normalement

## 🚀 Déploiement en Production

Pour la production, utilisez:
1. **SendGrid** (gratuit jusqu'à 100 emails/jour)
2. **Mailgun** (gratuit jusqu'à 5000 emails/mois)
3. **Amazon SES** (très économique)

## ⚠️ Limites

- **Gmail:** 500 emails/jour
- **Outlook:** 300 emails/jour
- **Yahoo:** 500 emails/jour
- **SendGrid Free:** 100 emails/jour

## 🐛 Dépannage

### Erreur: "Authentication failed"
- Vérifiez que vous utilisez un App Password (pas votre mot de passe normal)
- Vérifiez que l'authentification 2FA est activée sur Gmail

### Erreur: "Connection refused"
- Vérifiez le SMTP_HOST et SMTP_PORT
- Vérifiez votre connexion internet
- Vérifiez que le port 587 n'est pas bloqué par un firewall

### Les emails arrivent dans les spams
- Configurez SPF, DKIM et DMARC pour votre domaine
- Utilisez un service professionnel comme SendGrid
- Évitez les mots "spam" dans le contenu

## 📝 Exemple de Fichier .env Complet

```env
# Database
DATABASE_URL=mysql+pymysql://smartrecruit:password@localhost:3306/smartrecruitme

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# GitHub API
GITHUB_TOKEN=ghp_votre_token_github

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre-email@gmail.com
SMTP_PASSWORD=xxxx xxxx xxxx xxxx
FROM_EMAIL=votre-email@gmail.com
FROM_NAME=SmartRecruitMe
```

## ✅ Checklist de Configuration

- [ ] Créer un App Password Gmail
- [ ] Ajouter les variables SMTP dans .env
- [ ] Installer les dépendances email
- [ ] Tester avec test_email.py
- [ ] Créer une offre de test
- [ ] Vérifier la réception des emails
- [ ] Vérifier les logs du backend

## 🎉 Résultat Final

Une fois configuré, chaque nouvelle offre d'emploi déclenche automatiquement:
1. ✅ Création de l'offre dans la base de données
2. ✅ Envoi d'emails à tous les candidats (en arrière-plan)
3. ✅ Logs de confirmation dans la console
4. ✅ Les candidats reçoivent un email professionnel et stylisé
