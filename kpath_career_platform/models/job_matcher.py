import streamlit as st
from models import resume_parser

# --- Page Config ---
st.set_page_config(page_title="Job Matcher", page_icon="🔍", layout="wide")

# --- Back Button ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("🔍 Job Matcher")

st.write("Find jobs that match your skills and qualifications.")

# --- Upload Resume ---
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    import PyPDF2

    # Extract text
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + " "

    # Parse resume
    resume_info = resume_parser.extract_resume_info(resume_text)

    st.subheader("📌 Your Skills Extracted")
    st.write(", ".join(resume_info["tech_skills"]))

    # --- Job Database (example) ---
    jobs = [
        {"title": "Data Scientist", "skills": ["python", "sql", "machine learning"]},
        {"title": "Frontend Developer", "skills": ["javascript", "react", "html", "css"]},
        {"title": "Backend Developer", "skills": ["java", "sql", "cloud"]},
        {"title": "AI/ML Engineer", "skills": ["python", "deep learning", "nlp"]},
        {"title": "Data Analyst", "skills": ["python", "sql", "excel"]},
    ]

    st.subheader("🎯 Job Matches")
    candidate_skills = set(resume_info["tech_skills"])
    matched_jobs = []

    for job in jobs:
        overlap = candidate_skills.intersection(set(job["skills"]))
        if overlap:
            matched_jobs.append((job["title"], overlap))

    if matched_jobs:
        for job, overlap in matched_jobs:
            st.success(f"✅ {job} (Matched Skills: {', '.join(overlap)})")
    else:
        st.warning("⚠️ No strong matches found. Try learning more in-demand skills.")
