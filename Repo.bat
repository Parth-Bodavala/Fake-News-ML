@echo off
echo ==============================
echo  Setting up Fake-News-ML Repo
echo ==============================

git init

echo # Ignore datasets and pickle files > .gitignore
echo *.csv >> .gitignore
echo *.pkl >> .gitignore

echo pandas > requirements.txt
echo scikit-learn >> requirements.txt
echo nltk >> requirements.txt
echo streamlit >> requirements.txt

echo # 📰 Fake News Detection (ML + Streamlit) > README.md
echo. >> README.md
echo A Machine Learning project that detects whether a news article is REAL or FAKE using NLP and a Passive Aggressive Classifier. >> README.md

git add .
git commit -m "Initial commit - Fake News Detection ML project"

git branch -M main
git remote add origin https://github.com/Parth-Bodavala/Fake-News-ML.git

REM ⚠️ Force push overwrites GitHub repo
git push -u origin main --force

echo ==============================
echo   ✅ Repo setup complete (Forced)!
echo ==============================
pause
