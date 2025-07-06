from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .utils import preprocess_text

def match_resumes(resume_texts, job_desc):
    # Preprocess everything
    job_desc_clean = preprocess_text(job_desc)
    resume_cleaned = [preprocess_text(text) for text in resume_texts]

    # Combine all for vectorization
    all_texts = [job_desc_clean] + resume_cleaned
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Cosine similarity: resumes vs job description (0th index)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return similarities[0]
