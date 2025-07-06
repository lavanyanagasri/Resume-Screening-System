# 🧠 ResumeMatch AI – Intelligent Resume Screener

A smart AI-powered tool that matches uploaded resumes with a job description and ranks them based on skill and content similarity. Built using NLP, LLMs, and Streamlit for HR teams, recruiters, and job-seeking platforms.

---

## 🔍 Features

- 📄 Upload multiple resumes (PDF, DOCX, TXT)
- 🧠 Extracts text and key skills from resumes
- 🎯 Matches resumes against a job description
- 📊 Visual skill match analysis using bar charts
- 🤖 Generates AI-based resume feedback using Gemini (optional)
- 📥 Download match results as a CSV file

---

## 🚀 Live Demo

🔗 [Click here to open the deployed app](https://your-username-resume-screening-system.streamlit.app)

---

## 🛠️ Tech Stack

| Tool / Library         | Purpose                             |
|------------------------|-------------------------------------|
| Streamlit              | Web UI frontend                     |
| Python                 | Backend logic                       |
| NLTK                   | Text preprocessing                  |
| scikit-learn           | Cosine similarity & ML utilities    |
| docx2txt, PyPDF2       | Resume parsing (.docx/.pdf)         |
| pdfminer.six           | Advanced PDF parsing                |
| pandas                 | Data processing                     |
| google-generativeai    | Gemini LLM feedback generation      |
| python-dotenv          | Local API key management (.env)     |

---


---

## 🧑‍💻 Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ResumeMatch-AI.git
cd ResumeMatch-AI

```

🤖 AI Resume Feedback
You can optionally use Google Gemini to generate smart feedback for each resume.

How to Enable Gemini:
Get your API key from: https://makersuite.google.com/app/apikey

Add it to .env file:
```bash
GEMINI_API_KEY=your_key_here
```

📥 Output

Visual skill match chart

Ranked resume match scores

Resume feedback (if enabled)

Downloadable CSV report

👤 Author

Lavanya Naga Sri

💻 Full Stack & AI Enthusiast
