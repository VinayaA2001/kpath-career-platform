import streamlit as st
import PyPDF2
from models import resume_parser
from utils import db

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")


# Optional: enable OpenAI embeddings for better skill matching
USE_AI_MATCHING = False

st.title("🎯 Career Matchmaking & Skill Gap Analyzer")

# --- Upload Resume ---
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

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
        st.markdown("**💼 Experience / Organizations:**")
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

        # Extract required skills from JD (simple keyword match)
        jd_skills = [skill for skill in resume_parser.TECH_SKILLS if skill in jd_text_lower]

        # Compare with candidate skills
        candidate_skills = resume_info["tech_skills"]

        if USE_AI_MATCHING:
            from models.resume_parser import semantic_similarity
            matching_skills = []
            missing_skills = []
            for skill in jd_skills:
                score = semantic_similarity(" ".join(candidate_skills), skill)
                if score >= 0.7:
                    matching_skills.append(skill)
                else:
                    missing_skills.append(skill)
        else:
            matching_skills = [s for s in candidate_skills if s in jd_skills]
            missing_skills = [s for s in jd_skills if s not in candidate_skills]

        # Display results
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
