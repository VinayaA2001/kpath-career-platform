import streamlit as st
import PyPDF2
from models import resume_parser
from utils import db


# --- Page Title ---
st.title("📂 Resume Analyzer")

# Back to Home
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

# --- Upload Resume ---
uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text + " "

    # --- Parse Resume Info ---
    resume_info = resume_parser.extract_resume_info(resume_text)

    # --- Candidate Name ---
    candidate_name = st.text_input("👤 Enter your name", "Candidate")

    # --- Save to Database ---
    db.init_db()   # initialize once (creates table if needed)
    if st.button("💾 Save to Database"):
        db.save_resume(candidate_name, resume_info)  # ✅ no conn needed
        st.success("✅ Resume saved successfully!")

    # --- Display Resume Summary ---
    st.subheader("📌 Resume Summary")

    if resume_info["qualifications"]:
        st.markdown("**🎓 Qualifications:**")
        for q in resume_info["qualifications"]:
            st.write(f"- {q}")

    if resume_info["tech_skills"]:
        st.markdown("**🛠 Technical Skills:**")
        for s in resume_info["tech_skills"]:
            st.write(f"- {s}")

    if resume_info["soft_skills"]:
        st.markdown("**🤝 Soft Skills:**")
        for s in resume_info["soft_skills"]:
            st.write(f"- {s}")

    if resume_info["organizations"]:
        st.markdown("**💼 Organizations / Experience:**")
        for e in resume_info["organizations"]:
            st.write(f"- {e}")

    if resume_info["certifications"]:
        st.markdown("**🏅 Certifications:**")
        for c in resume_info["certifications"]:
            st.write(f"- {c}")

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
        jd_skills = [skill for skill in resume_parser.TECH_SKILLS if skill in jd_text_lower]
        candidate_skills = resume_info["tech_skills"]

        matching_skills = [s for s in candidate_skills if s in jd_skills]
        missing_skills = [s for s in jd_skills if s not in candidate_skills]

        st.markdown("**✅ Matching Skills:**")
        if matching_skills:
            for s in matching_skills:
                st.write(f"- {s}")
        else:
            st.write("None found.")

        st.markdown("**⚠️ Missing Skills (to improve for this job):**")
        if missing_skills:
            for s in missing_skills:
                st.write(f"- {s}")
        else:
            st.success("🎉 No major skill gaps detected!")

# --- View Saved Resumes Section ---
st.subheader("📂 View Saved Resumes")
if st.button("📋 Show All Resumes"):
    resumes = db.fetch_all_resumes()
    if resumes:
        st.dataframe(resumes)  # nice table view
    else:
        st.info("No resumes found in the database.")
