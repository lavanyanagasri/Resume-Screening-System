import streamlit as st
from src.parser import parse_resume
from src.matcher import match_resumes
from src.utils import preprocess_text, extract_skills
from src.feedback import generate_resume_feedback
import tempfile
import os
import pandas as pd

st.set_page_config(page_title="ResumeMatch AI", layout="centered")
st.title("🧠 ResumeMatch AI – Intelligent Resume Screener")

# --- Job Description Input ---
st.subheader("📌 Enter Job Description")
job_desc = st.text_area("Paste the job description here", height=200)

# --- Resume Upload ---
st.subheader("📁 Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload multiple resumes (.pdf, .docx, .txt)", 
    type=['pdf', 'docx', 'txt'], 
    accept_multiple_files=True
)

# --- Process ---
if st.button("🔍 Match Resumes"):
    if not job_desc or not uploaded_files:
        st.warning("⚠️ Please provide both job description and resumes.")
    else:
        st.info("⏳ Processing resumes...")

        resumes = []
        resume_names = []

        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(file.read())
                tmp_path = tmp_file.name

            resume_text = parse_resume(tmp_path)
            os.remove(tmp_path)

            if resume_text.strip():
                resumes.append(resume_text)
                resume_names.append(file.name)

        if resumes:
            # Cosine similarity scores
            scores = match_resumes(resumes, job_desc)

            # Skill match analysis
            st.subheader("🔬 Skill Match Analysis")
            jd_skills = extract_skills(job_desc)
            st.write(f"🔍 **Skills in Job Description**: {', '.join(jd_skills) if jd_skills else 'None detected'}")

            skill_summary = []
            for name, text in zip(resume_names, resumes):
                matched = extract_skills(text)
                score = len(set(matched) & set(jd_skills)) / len(jd_skills) if jd_skills else 0
                skill_summary.append({"Resume": name, "Skill Match %": round(score * 100, 2)})

            df = pd.DataFrame(skill_summary)

            if not df.empty:
                st.bar_chart(df.set_index("Resume"))

            # Filter: Top matches
            st.subheader("🎯 Filter by Match Score")
            min_score = st.slider("Minimum Match Score (%)", 0, 100, 60)

            filtered_results = [
                (name, score) for name, score in zip(resume_names, scores)
                if score * 100 >= min_score
            ]

            st.subheader("📊 Ranked Results")
            st.write(f"Showing {len(filtered_results)} resumes with score ≥ {min_score}%")

            for name, score in sorted(filtered_results, key=lambda x: x[1], reverse=True):
                match_pct = round(score * 100, 2)
                color = "🟩" if match_pct >= 75 else "🟨" if match_pct >= 50 else "🟥"
                st.write(f"{color} **{name}** → Match Score: `{match_pct}%`")

            # --- CSV Download ---
            st.subheader("📥 Download Results")
            csv_df = pd.DataFrame({
                "Resume": resume_names,
                "Match Score (%)": [round(score * 100, 2) for score in scores]
            })

            if 'skill_summary' in locals():
                skill_df = pd.DataFrame(skill_summary)
                csv_df = pd.merge(csv_df, skill_df, on="Resume", how="left")

            csv = csv_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📄 Download CSV",
                data=csv,
                file_name='resume_match_results.csv',
                mime='text/csv',
            )

            # --- AI-Powered Feedback ---
            st.subheader("🧠 AI-Powered Resume Feedback")

            for name, text in zip(resume_names, resumes):
                with st.expander(f"📄 {name} – View Feedback"):
                    with st.spinner("Generating feedback..."):
                        try:
                            feedback = generate_resume_feedback(text, job_desc)
                            st.markdown(feedback)
                        except Exception as e:
                            st.error(f"❌ Failed to generate feedback for {name}: {str(e)}")

        else:
            st.error("❌ Could not extract text from any resume.")
