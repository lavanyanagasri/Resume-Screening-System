from src.parser import parse_resume
from src.utils import load_job_description
from src.matcher import match_resumes
import os

# Load job description
job_desc = load_job_description()

resume_folder = "data/resumes"
resumes = []
resume_names = []

print("\n🔍 Reading resumes...\n")

for file in os.listdir(resume_folder):
    if file.endswith(('.pdf', '.docx', '.txt')):
        path = os.path.join(resume_folder, file)
        print(f"Found: {file}")
        text = parse_resume(path)
        if text.strip():
            print(f"✅ {file} has text ✅")
            resumes.append(text)
            resume_names.append(file)
        else:
            print(f"⚠️ {file} is EMPTY ⚠️")

if not resumes:
    print("❌ No valid resumes found. Please check your files.")
    exit()

scores = match_resumes(resumes, job_desc)

print("\n🔎 Resume Match Results:")
for i, score in enumerate(scores):
    print(f"{resume_names[i]} => {round(score * 100, 2)}% match")
