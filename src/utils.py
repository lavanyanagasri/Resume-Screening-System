import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS]
    return " ".join(tokens)

def extract_skills(text):
    skill_keywords = [
        "python", "machine learning", "deep learning", "data analysis",
        "pandas", "numpy", "scikit-learn", "tensorflow", "keras",
        "sql", "tableau", "matplotlib", "seaborn", "nlp", "flask",
        "django", "api", "cloud", "aws", "azure"
    ]
    text = preprocess_text(text)
    return [skill for skill in skill_keywords if skill in text]
