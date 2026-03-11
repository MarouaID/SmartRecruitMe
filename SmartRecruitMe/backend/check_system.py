"""
Script de vérification du système SmartRecruitMe
Exécuter: python check_system.py
"""

import sys
import subprocess
import importlib

def check_python_version():
    print("🐍 Vérification de Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} (requis: 3.11+)")
        return False

def check_package(package_name, import_name=None):
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"   ✅ {package_name}")
        return True
    except ImportError:
        print(f"   ❌ {package_name} (manquant)")
        return False

def check_backend_packages():
    print("\n📦 Vérification des packages backend...")
    packages = [
        ("FastAPI", "fastapi"),
        ("Uvicorn", "uvicorn"),
        ("SQLAlchemy", "sqlalchemy"),
        ("Pydantic", "pydantic"),
        ("Redis", "redis"),
        ("spaCy", "spacy"),
        ("pdfplumber", "pdfplumber"),
        ("python-docx", "docx"),
        ("requests", "requests"),
        ("scikit-learn", "sklearn"),
    ]
    
    results = []
    for name, import_name in packages:
        results.append(check_package(name, import_name))
    
    return all(results)

def check_spacy_model():
    print("\n🧠 Vérification du modèle spaCy...")
    try:
        import spacy
        nlp = spacy.load("en_core_web_md")
        print("   ✅ Modèle en_core_web_md chargé")
        return True
    except:
        print("   ❌ Modèle en_core_web_md manquant")
        print("   💡 Exécuter: python -m spacy download en_core_web_md")
        return False

def check_docker():
    print("\n🐳 Vérification de Docker...")
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {result.stdout.strip()}")
            return True
        else:
            print("   ❌ Docker non trouvé")
            return False
    except FileNotFoundError:
        print("   ❌ Docker non installé")
        return False

def check_docker_compose():
    print("\n🐳 Vérification de Docker Compose...")
    try:
        result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {result.stdout.strip()}")
            return True
        else:
            print("   ❌ Docker Compose non trouvé")
            return False
    except FileNotFoundError:
        print("   ❌ Docker Compose non installé")
        return False

def check_env_file():
    print("\n⚙️  Vérification des fichiers de configuration...")
    import os
    
    backend_env = os.path.exists("backend/.env")
    frontend_env = os.path.exists("frontend/.env")
    
    if backend_env:
        print("   ✅ backend/.env")
    else:
        print("   ⚠️  backend/.env manquant (optionnel)")
    
    if frontend_env:
        print("   ✅ frontend/.env")
    else:
        print("   ⚠️  frontend/.env manquant (optionnel)")
    
    return True

def main():
    print("=" * 60)
    print("  SmartRecruitMe - Vérification du Système")
    print("=" * 60)
    
    results = []
    
    results.append(check_python_version())
    results.append(check_backend_packages())
    results.append(check_spacy_model())
    results.append(check_docker())
    results.append(check_docker_compose())
    results.append(check_env_file())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ Tous les tests sont passés!")
        print("🚀 Vous pouvez démarrer le projet avec: docker-compose up")
    else:
        print("⚠️  Certains composants sont manquants")
        print("📖 Consultez le README.md pour les instructions d'installation")
    print("=" * 60)

if __name__ == "__main__":
    main()
