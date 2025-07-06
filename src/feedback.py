import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_resume_feedback(resume_text, job_description):
    prompt = f"""
You are a recruiter reviewing a resume for a job opening.

Job Description:
{job_description}

Resume:
{resume_text}

Give 3 bullet points:
1. Strengths
2. Missing or weak areas
3. Suggestions to improve resume for this JD
"""

    try:
        # ✅ Use correct model name from your list
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Failed to generate feedback: {str(e)}"
