@echo off
echo ========================================
echo   SmartRecruitMe - Demarrage Rapide
echo ========================================
echo.

echo Verification de Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Docker n'est pas installe ou n'est pas dans le PATH
    echo Veuillez installer Docker Desktop depuis https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo Docker detecte!
echo.

echo Demarrage des services avec Docker Compose...
echo Cela peut prendre 2-3 minutes la premiere fois...
echo.

cd SmartRecruitMe
docker-compose up --build

pause
