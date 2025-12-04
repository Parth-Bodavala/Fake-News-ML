import streamlit as st
import string
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def ensure_nltk_resource(name, download_name=None):
    import nltk.data
    try:
        nltk.data.find(name)
    except:
        nltk.download(download_name or name.split('/')[-1])

ensure_nltk_resource('corpora/stopwords', 'stopwords')
ensure_nltk_resource('corpora/wordnet', 'wordnet')
ensure_nltk_resource('corpora/omw-1.4', 'omw-1.4')

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = ''.join(c for c in text if c not in string.punctuation)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words).strip()

@st.cache_resource
def load_artifacts(model_path="model.pkl", vectorizer_path="vectorizer.pkl"):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_artifacts()

st.set_page_config(page_title="Fake News Detection", layout="centered")
st.title("📰 Fake News Detection Web App")

st.markdown("Enter the news content below and click **Check** to detect if it's real or fake.")

input_text = st.text_area("📝 News Text", height=220)

if st.button("Check"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some news content.")
    else:
        cleaned = clean_text(input_text)
        vectorized = vectorizer.transform([cleaned])

        if vectorized.nnz == 0:
            st.warning("⚠️ Not enough meaningful words to analyze this news.")
        else:
            prediction = model.predict(vectorized)[0].strip().lower()

            if prediction == "fake":
                st.error("❌ This news is likely **FAKE**.")
            else:
                st.success("✅ This news is likely **REAL**.")
