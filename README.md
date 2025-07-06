title: "🧠 ResumeMatch AI – Intelligent Resume Screener"
description: >
  A smart AI-powered tool that matches uploaded resumes with a job description and ranks them
  based on skill and content similarity. Built using NLP, LLMs, and Streamlit for HR teams,
  recruiters, and job-seeking platforms.

features:
  - "📄 Upload multiple resumes (PDF, DOCX, TXT)"
  - "🧠 Extracts text and key skills from resumes"
  - "🎯 Matches resumes against a job description"
  - "📊 Visual skill match analysis using bar charts"
  - "🤖 Generates feedback using Gemini / LLMs (optional)"
  - "📥 Download match results as a CSV"

live_demo: "https://your-username-resume-screening-system.streamlit.app"

tech_stack:
  - Streamlit
  - nltk
  - scikit-learn
  - docx2txt
  - PyPDF2
  - pdfminer.six
  - pandas
  - google-generativeai
  - python-dotenv

project_structure: |
  ResumeMatch-AI/
  ├── app.py                  # Streamlit main app
  ├── requirements.txt
  ├── .streamlit/             # Optional: theme config
  ├── src/
  │   ├── parser.py           # Resume file parsing
  │   ├── matcher.py          # Cosine similarity logic
  │   ├── utils.py            # Preprocessing, skill extraction
  │   └── feedback.py         # Gemini feedback generation
  └── data/resumes/           # Sample resumes

how_to_run:
  - "Clone the repo"
  - "cd ResumeMatch-AI"
  - "pip install -r requirements.txt"
  - "Create .env file (optional): GEMINI_API_KEY=your_key_here"
  - "streamlit run app.py"

gemini_feedback:
  description: >
    If you want AI-based resume feedback, use a Google Gemini API key. 
    Store it in a .env file locally or as a secret in Streamlit Cloud.
  link: "https://makersuite.google.com/app/apikey"

output:
  - "📊 Skill Match Bar Chart"
  - "📥 Downloadable CSV with Match Scores"
  - "🤖 Optional LLM-powered Resume Feedback"

author:
  name: "Lavanya Naga Sri"
  role: "Passionate developer building AI tools to empower hiring and job applications."

license: "MIT License – use freely with credit 🌱"
