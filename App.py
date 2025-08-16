import streamlit as st
import pandas as pd
import string
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

#stopwords and lemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Load model and vectorizer
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation and not c.isdigit()])
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text.strip()

# Streamlit UI
st.set_page_config(page_title="Fake News Detection", layout="centered")
st.title("📰 Fake News Detection Web App")

st.markdown("Enter the news content below and click **Check** to detect if it's real or fake.")

# Input text area
input_text = st.text_area("📝 News Text", height=200)

if st.button("Check"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some news content.")
    else:
        # Preprocess and predict
        cleaned = clean_text(input_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction.upper() == "FAKE":
            st.error(f"❌ This news is likely **FAKE**.")
        else:
            st.success(f"✅ This news is likely **REAL**.")