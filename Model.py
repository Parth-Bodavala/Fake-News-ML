import pandas as pd
import string
import pickle
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Load datasets
fake_df = pd.read_csv('Fake.csv')
real_df = pd.read_csv('True.csv')

# Add labels
fake_df['label'] = 'FAKE'
real_df['label'] = 'REAL'

# Combine datasets
df = pd.concat([fake_df, real_df], ignore_index=True)
df = df[['text', 'label']].dropna().drop_duplicates()

# Clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation and not c.isdigit()])
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text.strip()

df['cleaned_text'] = df['text'].apply(clean_text)

# TF-IDF vectorization with improved settings
vectorizer = TfidfVectorizer(max_df=0.7, min_df=5, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['cleaned_text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (Passive Aggressive Classifier)
model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Training complete. Model and vectorizer saved.")