@echo off
echo ==============================
echo  Setting up Fake-News-ML Repo
echo ==============================

REM Step 1: Initialize Git
git init

REM Step 2: Create .gitignore
echo # Ignore datasets and pickle files > .gitignore
echo *.csv >> .gitignore
echo *.pkl >> .gitignore

REM Step 3: Create requirements.txt
echo pandas > requirements.txt
echo scikit-learn >> requirements.txt
echo nltk >> requirements.txt
echo streamlit >> requirements.txt

REM Step 4: Create README.md
echo # 📰 Fake News Detection (ML + Streamlit) > README.md
echo. >> README.md
echo A Machine Learning project that detects whether a news article is **REAL** or **FAKE** using NLP and a Passive Aggressive Classifier. >> README.md
echo. >> README.md
echo ## 🚀 Features >> README.md
echo - Text preprocessing (stopword removal, lemmatization, cleaning) >> README.md
echo - TF-IDF vectorization >> README.md
echo - Passive Aggressive Classifier for fake news detection >> README.md
echo - Interactive web app built with Streamlit >> README.md
echo. >> README.md
echo ## ▶️ Run Locally >> README.md
echo \`\`\`bash >> README.md
echo pip install -r requirements.txt >> README.md
echo streamlit run App.py >> README.md
echo \`\`\` >> README.md

REM Step 5: Git commit and push
git add .
git commit -m "Initial commit - Fake News Detection ML project"
git branch -M main
git remote add origin https://github.com/Parth-Bodavala/Fake-News-ML.git
git push -u origin main

echo ==============================
echo   ✅ Repo setup complete!
echo ==============================
pause