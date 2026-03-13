"""
Service d'envoi d'emails pour SmartRecruitMe
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class EmailService:
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = os.getenv("SMTP_USER", "")
        self.smtp_password = os.getenv("SMTP_PASSWORD", "")
        self.from_email = os.getenv("FROM_EMAIL", self.smtp_user)
        self.from_name = os.getenv("FROM_NAME", "SmartRecruitMe")
        
    def send_email(self, to_email: str, subject: str, html_content: str, text_content: str = None) -> bool:
        """
        Envoie un email
        """
        # Mode démonstration si pas de configuration
        if not self.smtp_user or not self.smtp_password:
            print(f"📧 [MODE DEMO] Email simulé à {to_email}")
            print(f"   Sujet: {subject}")
            print(f"   ✅ Email non envoyé (configuration SMTP manquante)")
            return True  # Retourner True pour ne pas bloquer l'application
        
        try:
            # Créer le message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = f"{self.from_name} <{self.from_email}>"
            message["To"] = to_email
            
            # Ajouter le contenu texte
            if text_content:
                part1 = MIMEText(text_content, "plain")
                message.attach(part1)
            
            # Ajouter le contenu HTML
            part2 = MIMEText(html_content, "html")
            message.attach(part2)
            
            # Envoyer l'email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                if self.smtp_user and self.smtp_password:
                    server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)
            
            print(f"✅ Email envoyé à {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de l'envoi de l'email à {to_email}: {e}")
            return False
    
    def send_new_job_notification(self, candidate_email: str, candidate_name: str, 
                                   job_title: str, company_name: str, 
                                   job_description: str, required_skills: List[str],
                                   location: str, contract_type: str) -> bool:
        """
        Envoie une notification de nouvelle offre d'emploi à un candidat
        """
        subject = f"🎯 Nouvelle offre: {job_title} chez {company_name}"
        
        # Contenu HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px 10px 0 0;
                    text-align: center;
                }}
                .header h1 {{
                    margin: 0;
                    font-size: 24px;
                }}
                .content {{
                    background: #f9fafb;
                    padding: 30px;
                    border-radius: 0 0 10px 10px;
                }}
                .job-card {{
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .job-title {{
                    color: #667eea;
                    font-size: 22px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }}
                .company {{
                    color: #666;
                    font-size: 16px;
                    margin-bottom: 15px;
                }}
                .info-row {{
                    display: flex;
                    margin: 10px 0;
                    padding: 8px 0;
                    border-bottom: 1px solid #eee;
                }}
                .info-label {{
                    font-weight: bold;
                    color: #667eea;
                    min-width: 120px;
                }}
                .skills {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-top: 10px;
                }}
                .skill-tag {{
                    background: #667eea;
                    color: white;
                    padding: 5px 12px;
                    border-radius: 20px;
                    font-size: 12px;
                }}
                .description {{
                    margin: 15px 0;
                    padding: 15px;
                    background: #f9fafb;
                    border-left: 4px solid #667eea;
                    border-radius: 4px;
                }}
                .cta-button {{
                    display: inline-block;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 15px 30px;
                    text-decoration: none;
                    border-radius: 25px;
                    font-weight: bold;
                    margin: 20px 0;
                    text-align: center;
                }}
                .footer {{
                    text-align: center;
                    color: #666;
                    font-size: 12px;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #eee;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🎯 Nouvelle Opportunité pour Vous!</h1>
            </div>
            
            <div class="content">
                <p>Bonjour <strong>{candidate_name}</strong>,</p>
                
                <p>Une nouvelle offre d'emploi vient d'être publiée sur SmartRecruitMe et pourrait vous intéresser!</p>
                
                <div class="job-card">
                    <div class="job-title">{job_title}</div>
                    <div class="company">📍 {company_name}</div>
                    
                    <div class="info-row">
                        <span class="info-label">📍 Localisation:</span>
                        <span>{location}</span>
                    </div>
                    
                    <div class="info-row">
                        <span class="info-label">📝 Type de contrat:</span>
                        <span>{contract_type}</span>
                    </div>
                    
                    <div class="description">
                        <strong>Description:</strong><br>
                        {job_description[:300]}{'...' if len(job_description) > 300 else ''}
                    </div>
                    
                    <div>
                        <strong class="info-label">🔧 Compétences requises:</strong>
                        <div class="skills">
                            {''.join([f'<span class="skill-tag">{skill}</span>' for skill in required_skills[:8]])}
                        </div>
                    </div>
                </div>
                
                <center>
                    <a href="http://localhost:3000/candidate/jobs" class="cta-button">
                        Voir l'offre complète →
                    </a>
                </center>
                
                <p style="margin-top: 30px; color: #666;">
                    💡 <strong>Conseil:</strong> Connectez-vous à votre profil pour voir votre score de compatibilité avec cette offre!
                </p>
            </div>
            
            <div class="footer">
                <p>Vous recevez cet email car vous êtes inscrit sur SmartRecruitMe.</p>
                <p>© 2025 SmartRecruitMe - Plateforme Intelligente de Recrutement</p>
            </div>
        </body>
        </html>
        """
        
        # Contenu texte (fallback)
        text_content = f"""
        Bonjour {candidate_name},
        
        Une nouvelle offre d'emploi vient d'être publiée sur SmartRecruitMe!
        
        Poste: {job_title}
        Entreprise: {company_name}
        Localisation: {location}
        Type de contrat: {contract_type}
        
        Compétences requises: {', '.join(required_skills)}
        
        Description:
        {job_description[:200]}...
        
        Connectez-vous sur http://localhost:3000 pour voir l'offre complète et votre score de compatibilité!
        
        Cordialement,
        L'équipe SmartRecruitMe
        """
        
        return self.send_email(candidate_email, subject, html_content, text_content)
    
    def send_bulk_new_job_notifications(self, candidates: List[dict], job_data: dict) -> dict:
        """
        Envoie des notifications à plusieurs candidats
        """
        results = {
            "total": len(candidates),
            "sent": 0,
            "failed": 0,
            "errors": []
        }
        
        for candidate in candidates:
            success = self.send_new_job_notification(
                candidate_email=candidate["email"],
                candidate_name=candidate["name"],
                job_title=job_data["title"],
                company_name=job_data["company"],
                job_description=job_data["description"],
                required_skills=job_data["required_skills"],
                location=job_data["location"],
                contract_type=job_data["contract_type"]
            )
            
            if success:
                results["sent"] += 1
            else:
                results["failed"] += 1
                results["errors"].append(candidate["email"])
        
        return results

# Instance globale
email_service = EmailService()
