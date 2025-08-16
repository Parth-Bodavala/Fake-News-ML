@echo off
echo ==============================
echo  Setting up Fake-News-ML Repo
echo ==============================

REM Step 1: Initialize Git
git init

REM Step 2: Create .gitignore (only ignore .pkl files now)
echo # Ignore pickle model files > .gitignore
echo *.pkl >> .gitignore

REM Step 3: Create requirements.txt
echo pandas > requirements.txt
echo scikit-learn >> requirements.txt
echo nltk >> requirements.txt
echo streamlit >> requirements.txt

REM Step 4: Create README.md
echo # 📰 Fake News Detection (ML + Streamlit) > README.md
echo. >> README.md
echo A Machine Learning project that detects whether a news article is REAL or FAKE using NLP and a Passive Aggressive Classifier. >> README.md

REM Step 5: Git commit
git add .
git commit -m "Initial commit - Fake News Detection ML project with datasets"

REM Step 6: Link remote and sync
git branch -M main
git remote add origin https://github.com/Parth-Bodavala/Fake-News-ML.git

REM Pull existing commits (like README) before pushing
git pull origin main --rebase

REM Push to GitHub
git push -u origin main

echo ==============================
echo   ✅ Repo setup complete (CSV included)!
echo ==============================
pause
