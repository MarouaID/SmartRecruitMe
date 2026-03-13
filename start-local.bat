@echo off
echo ========================================
echo   SmartRecruitMe - Demarrage Rapide
echo   (Sans Docker - Mode Developpement)
echo ========================================
echo.

echo [1/4] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe
    echo Telechargez Python depuis https://www.python.org/downloads/
    pause
    exit /b 1
)
echo OK - Python detecte
echo.

echo [2/4] Verification de Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Node.js n'est pas installe
    echo Telechargez Node.js depuis https://nodejs.org/
    pause
    exit /b 1
)
echo OK - Node.js detecte
echo.

echo [3/4] Installation des dependances backend...
cd SmartRecruitMe\backend
if not exist venv (
    echo Creation de l'environnement virtuel...
    python -m venv venv
)

call venv\Scripts\activate
pip install -r requirements.txt --quiet
python -m spacy download en_core_web_md --quiet

echo OK - Backend pret
echo.

echo [4/4] Installation des dependances frontend...
cd ..\frontend
if not exist node_modules (
    echo Installation de npm packages...
    call npm install --silent
)
echo OK - Frontend pret
echo.

echo ========================================
echo   DEMARRAGE DE L'APPLICATION
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Appuyez sur Ctrl+C pour arreter
echo.

start "SmartRecruitMe Backend" cmd /k "cd /d %~dp0SmartRecruitMe\backend && venv\Scripts\activate && python seed_data.py && uvicorn app.main:app --reload"
timeout /t 5 /nobreak >nul
start "SmartRecruitMe Frontend" cmd /k "cd /d %~dp0SmartRecruitMe\frontend && npm start"

echo.
echo L'application va s'ouvrir dans votre navigateur...
echo.
pause
