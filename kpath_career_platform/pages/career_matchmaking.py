import streamlit as st
import PyPDF2
from models import resume_parser
from utils import db
from components import render_header, render_footer  # ✅ Reuse header & footer

# --- Page Config ---
st.set_page_config(page_title="Career Matchmaking", layout="wide")

# --- Header ---
render_header()

# --- Back Navigation ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")  # make sure `app.py` is at project root

# --- Title ---
st.title("🎯 Career Matchmaking & Skill Gap Analyzer")

# Optional: enable OpenAI embeddings for better skill matching
USE_AI_MATCHING = False

# --- Upload Resume ---
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = " ".join([page.extract_text() or "" for page in pdf_reader.pages])

    # --- Parse Resume Info ---
    resume_info = resume_parser.extract_resume_info(resume_text)

    # --- Store in DB ---
    conn = db.init_db()
    candidate_name = st.text_input("👤 Enter your name", "Candidate")
    if st.button("💾 Save to Database"):
        db.save_resume(conn, candidate_name, resume_info)
        st.success("Resume saved to database successfully ✅")

    # --- Display Resume Summary ---
    st.subheader("📌 Resume Summary")

    if resume_info["qualifications"]:
        st.markdown("**🎓 Qualifications:**")
        st.write("\n".join([f"- {q}" for q in resume_info["qualifications"]]))

    if resume_info["tech_skills"]:
        st.markdown("**🛠 Technical Skills:**")
        st.write("\n".join([f"- {s}" for s in resume_info["tech_skills"]]))

    if resume_info["soft_skills"]:
        st.markdown("**🤝 Soft Skills:**")
        st.write("\n".join([f"- {s}" for s in resume_info["soft_skills"]]))

    if resume_info["organizations"]:
        st.markdown("**💼 Experience / Organizations:**")
        st.write("\n".join([f"- {e}" for e in resume_info["organizations"]]))

    if resume_info["certifications"]:
        st.markdown("**🏅 Certifications:**")
        st.write("\n".join([f"- {c}" for c in resume_info["certifications"]]))

    st.markdown(f"**⌛ Years of Experience:** {resume_info['experience']} years")

    # --- Career Suggestions ---
    st.subheader("💡 Career Suggestions")
    suggested = resume_parser.suggest_careers(resume_info)
    for career in suggested:
        st.write(f"- {career}")

    # --- Skill Gap Analyzer ---
    st.subheader("🔍 Skill Gap Analyzer")
    jd_text = st.text_area("Paste a Job Description (JD) here:")

    if jd_text:
        jd_text_lower = jd_text.lower()

        # Extract required skills from JD (simple keyword match)
        jd_skills = [skill for skill in resume_parser.TECH_SKILLS if skill in jd_text_lower]

        # Compare with candidate skills
        candidate_skills = resume_info["tech_skills"]

        if USE_AI_MATCHING:
            from models.resume_parser import semantic_similarity
            matching_skills, missing_skills = [], []
            for skill in jd_skills:
                score = semantic_similarity(" ".join(candidate_skills), skill)
                (matching_skills if score >= 0.7 else missing_skills).append(skill)
        else:
            matching_skills = [s for s in candidate_skills if s in jd_skills]
            missing_skills = [s for s in jd_skills if s not in candidate_skills]

        # Display results
        st.markdown("**✅ Matching Skills:**")
        st.write("\n".join([f"- {s}" for s in matching_skills]) if matching_skills else "None found.")

        st.markdown("**⚠️ Missing Skills (to improve for this job):**")
        if missing_skills:
            st.write("\n".join([f"- {s}" for s in missing_skills]))
        else:
            st.success("🎉 No major skill gaps detected!")

# --- Footer ---
render_footer()
