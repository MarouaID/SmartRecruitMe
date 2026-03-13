"""
Script pour générer des CV de test au format texte
"""
from docx import Document
import os

def create_cv_1():
    """CV - Développeur Full Stack Junior"""
    doc = Document()
    
    doc.add_heading('Maroua IDOMAR', 0)
    doc.add_paragraph('Développeuse Full Stack Junior')
    doc.add_paragraph('Email: maroua.idomar@email.com | Tél: +212 6 12 34 56 78')
    doc.add_paragraph('GitHub: github.com/marouaidomar | LinkedIn: linkedin.com/in/marouaidomar')
    doc.add_paragraph('Localisation: Rabat, Maroc')
    
    doc.add_heading('Profil', 1)
    doc.add_paragraph(
        'Développeuse Full Stack passionnée avec 2 ans d\'expérience dans le développement '
        'd\'applications web modernes. Spécialisée en React, Node.js et Python avec une forte '
        'capacité d\'apprentissage et d\'adaptation aux nouvelles technologies.'
    )
    
    doc.add_heading('Expérience Professionnelle', 1)
    
    doc.add_heading('Développeuse Full Stack - TechStart Morocco', 2)
    doc.add_paragraph('Septembre 2022 - Présent | Casablanca, Maroc')
    doc.add_paragraph('• Développement d\'applications web avec React et Node.js')
    doc.add_paragraph('• Création d\'APIs RESTful avec Express et FastAPI')
    doc.add_paragraph('• Intégration de bases de données MongoDB et PostgreSQL')
    doc.add_paragraph('• Mise en place de tests unitaires avec Jest et Pytest')
    doc.add_paragraph('• Collaboration en équipe Agile/Scrum')
    
    doc.add_heading('Stage Développement Web - Digital Agency', 2)
    doc.add_paragraph('Juin 2021 - Août 2022 | Rabat, Maroc')
    doc.add_paragraph('• Développement de sites web responsive avec HTML, CSS, JavaScript')
    doc.add_paragraph('• Utilisation de frameworks comme Bootstrap et Tailwind CSS')
    doc.add_paragraph('• Maintenance et amélioration de sites existants')
    
    doc.add_heading('Formation', 1)
    doc.add_paragraph('Ingénieur en Génie Informatique - ENSA Tétouan')
    doc.add_paragraph('2018 - 2022')
    
    doc.add_heading('Compétences Techniques', 1)
    doc.add_paragraph('• Langages: JavaScript, Python, TypeScript, Java, SQL')
    doc.add_paragraph('• Frontend: React, Vue.js, HTML5, CSS3, Tailwind CSS, Bootstrap')
    doc.add_paragraph('• Backend: Node.js, Express, FastAPI, Django')
    doc.add_paragraph('• Bases de données: MongoDB, PostgreSQL, MySQL, Redis')
    doc.add_paragraph('• DevOps: Docker, Git, GitHub Actions, CI/CD')
    doc.add_paragraph('• Outils: VS Code, Postman, Figma, Jira')
    
    doc.add_heading('Projets', 1)
    doc.add_paragraph('• E-commerce Platform: Application complète avec React, Node.js et MongoDB')
    doc.add_paragraph('• Task Manager: Application de gestion de tâches avec authentification JWT')
    doc.add_paragraph('• Weather App: Application météo utilisant des APIs externes')
    
    doc.add_heading('Langues', 1)
    doc.add_paragraph('• Arabe: Langue maternelle')
    doc.add_paragraph('• Français: Courant')
    doc.add_paragraph('• Anglais: Professionnel')
    
    doc.save('cv_maroua_idomar.docx')
    print("✅ CV 1 créé: cv_maroua_idomar.docx")

def create_cv_2():
    """CV - Data Scientist"""
    doc = Document()
    
    doc.add_heading('Azar AGHRIB', 0)
    doc.add_paragraph('Data Scientist & Machine Learning Engineer')
    doc.add_paragraph('Email: azar.aghrib@email.com | Tél: +212 6 98 76 54 32')
    doc.add_paragraph('GitHub: github.com/azaraghrib | LinkedIn: linkedin.com/in/azaraghrib')
    doc.add_paragraph('Localisation: Casablanca, Maroc')
    
    doc.add_heading('Profil', 1)
    doc.add_paragraph(
        'Data Scientist avec 3 ans d\'expérience en analyse de données et développement de modèles '
        'de Machine Learning. Expert en Python, TensorFlow et analyse statistique. Passionné par '
        'l\'IA et les solutions data-driven pour résoudre des problèmes complexes.'
    )
    
    doc.add_heading('Expérience Professionnelle', 1)
    
    doc.add_heading('Data Scientist Senior - DataCorp', 2)
    doc.add_paragraph('Janvier 2022 - Présent | Casablanca, Maroc')
    doc.add_paragraph('• Développement de modèles de Machine Learning pour la prédiction de churn')
    doc.add_paragraph('• Analyse de données massives avec Python, Pandas et NumPy')
    doc.add_paragraph('• Création de dashboards interactifs avec Tableau et Power BI')
    doc.add_paragraph('• Déploiement de modèles ML en production avec Docker et Kubernetes')
    doc.add_paragraph('• Amélioration de 25% de la précision des modèles prédictifs')
    
    doc.add_heading('Data Analyst - FinTech Solutions', 2)
    doc.add_paragraph('Mars 2021 - Décembre 2021 | Rabat, Maroc')
    doc.add_paragraph('• Analyse de données financières et création de rapports')
    doc.add_paragraph('• Développement de scripts Python pour l\'automatisation')
    doc.add_paragraph('• Visualisation de données avec Matplotlib et Seaborn')
    doc.add_paragraph('• Collaboration avec les équipes métier pour définir les KPIs')
    
    doc.add_heading('Formation', 1)
    doc.add_paragraph('Master en Data Science & Big Data - Université Mohammed V')
    doc.add_paragraph('2019 - 2021')
    doc.add_paragraph('Licence en Mathématiques Appliquées - Faculté des Sciences')
    doc.add_paragraph('2016 - 2019')
    
    doc.add_heading('Compétences Techniques', 1)
    doc.add_paragraph('• Langages: Python, R, SQL, Scala')
    doc.add_paragraph('• Machine Learning: Scikit-learn, TensorFlow, PyTorch, Keras')
    doc.add_paragraph('• Data Processing: Pandas, NumPy, Apache Spark, Dask')
    doc.add_paragraph('• Visualisation: Matplotlib, Seaborn, Plotly, Tableau, Power BI')
    doc.add_paragraph('• Bases de données: PostgreSQL, MongoDB, MySQL, Redis')
    doc.add_paragraph('• Cloud: AWS (SageMaker, S3, EC2), Google Cloud Platform')
    doc.add_paragraph('• MLOps: Docker, Kubernetes, MLflow, Airflow')
    
    doc.add_heading('Certifications', 1)
    doc.add_paragraph('• AWS Certified Machine Learning - Specialty')
    doc.add_paragraph('• TensorFlow Developer Certificate')
    doc.add_paragraph('• Google Data Analytics Professional Certificate')
    
    doc.add_heading('Langues', 1)
    doc.add_paragraph('• Arabe: Langue maternelle')
    doc.add_paragraph('• Français: Courant')
    doc.add_paragraph('• Anglais: Avancé')
    
    doc.save('cv_azar_aghrib.docx')
    print("✅ CV 2 créé: cv_azar_aghrib.docx")

def create_cv_3():
    """CV - DevOps Engineer"""
    doc = Document()
    
    doc.add_heading('Youssef BENNANI', 0)
    doc.add_paragraph('DevOps Engineer & Cloud Architect')
    doc.add_paragraph('Email: youssef.bennani@email.com | Tél: +212 6 55 44 33 22')
    doc.add_paragraph('GitHub: github.com/youssefbennani | LinkedIn: linkedin.com/in/youssefbennani')
    doc.add_paragraph('Localisation: Rabat, Maroc')
    
    doc.add_heading('Profil', 1)
    doc.add_paragraph(
        'DevOps Engineer avec 4 ans d\'expérience dans l\'automatisation, le déploiement continu '
        'et la gestion d\'infrastructures cloud. Expert en Docker, Kubernetes, AWS et CI/CD. '
        'Passionné par l\'optimisation des processus et l\'amélioration de la fiabilité des systèmes.'
    )
    
    doc.add_heading('Expérience Professionnelle', 1)
    
    doc.add_heading('DevOps Engineer Senior - CloudTech', 2)
    doc.add_paragraph('Février 2021 - Présent | Rabat, Maroc')
    doc.add_paragraph('• Architecture et gestion d\'infrastructures AWS (EC2, S3, RDS, Lambda)')
    doc.add_paragraph('• Orchestration de containers avec Kubernetes et Docker Swarm')
    doc.add_paragraph('• Mise en place de pipelines CI/CD avec Jenkins, GitLab CI et GitHub Actions')
    doc.add_paragraph('• Automatisation avec Terraform, Ansible et Python')
    doc.add_paragraph('• Monitoring avec Prometheus, Grafana et ELK Stack')
    doc.add_paragraph('• Réduction de 40% du temps de déploiement')
    
    doc.add_heading('DevOps Engineer - StartupHub', 2)
    doc.add_paragraph('Juin 2020 - Janvier 2021 | Casablanca, Maroc')
    doc.add_paragraph('• Configuration et maintenance de serveurs Linux')
    doc.add_paragraph('• Containerisation d\'applications avec Docker')
    doc.add_paragraph('• Scripting Bash et Python pour l\'automatisation')
    doc.add_paragraph('• Gestion de bases de données PostgreSQL et MongoDB')
    
    doc.add_heading('Formation', 1)
    doc.add_paragraph('Ingénieur en Réseaux et Systèmes - ENSIAS')
    doc.add_paragraph('2016 - 2020')
    
    doc.add_heading('Compétences Techniques', 1)
    doc.add_paragraph('• Cloud: AWS, Azure, Google Cloud Platform')
    doc.add_paragraph('• Containers: Docker, Kubernetes, Docker Compose, Helm')
    doc.add_paragraph('• CI/CD: Jenkins, GitLab CI, GitHub Actions, CircleCI')
    doc.add_paragraph('• IaC: Terraform, Ansible, CloudFormation')
    doc.add_paragraph('• Monitoring: Prometheus, Grafana, ELK Stack, Datadog')
    doc.add_paragraph('• Scripting: Bash, Python, PowerShell')
    doc.add_paragraph('• OS: Linux (Ubuntu, CentOS, RHEL), Windows Server')
    doc.add_paragraph('• Bases de données: PostgreSQL, MySQL, MongoDB, Redis')
    doc.add_paragraph('• Version Control: Git, GitHub, GitLab, Bitbucket')
    
    doc.add_heading('Certifications', 1)
    doc.add_paragraph('• AWS Certified Solutions Architect - Associate')
    doc.add_paragraph('• Certified Kubernetes Administrator (CKA)')
    doc.add_paragraph('• HashiCorp Certified: Terraform Associate')
    doc.add_paragraph('• Docker Certified Associate')
    
    doc.add_heading('Projets', 1)
    doc.add_paragraph('• Migration complète d\'infrastructure on-premise vers AWS')
    doc.add_paragraph('• Mise en place d\'un cluster Kubernetes multi-région')
    doc.add_paragraph('• Automatisation complète du déploiement avec Terraform et Ansible')
    
    doc.add_heading('Langues', 1)
    doc.add_paragraph('• Arabe: Langue maternelle')
    doc.add_paragraph('• Français: Courant')
    doc.add_paragraph('• Anglais: Avancé')
    
    doc.save('cv_youssef_bennani.docx')
    print("✅ CV 3 créé: cv_youssef_bennani.docx")

if __name__ == "__main__":
    print("🚀 Génération des CV de test...\n")
    create_cv_1()
    create_cv_2()
    create_cv_3()
    print("\n✅ Tous les CV ont été générés avec succès!")
    print("📁 Les fichiers sont dans le dossier backend/")
