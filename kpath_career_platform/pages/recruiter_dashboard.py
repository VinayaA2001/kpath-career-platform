import streamlit as st
import sqlite3

st.title("📂 Resume Viewer + Candidate Ranking (Recruiter Mode)")

# --- Connect to database ---
def get_resumes():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("SELECT id, name, qualifications, skills, soft_skills, experience, certifications FROM resumes")
    rows = c.fetchall()
    conn.close()
    return rows

def search_resumes(keyword):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    query = """
        SELECT id, name, qualifications, skills, soft_skills, experience, certifications 
        FROM resumes 
        WHERE name LIKE ? OR skills LIKE ? OR soft_skills LIKE ? OR qualifications LIKE ? OR certifications LIKE ?
    """
    like_kw = f"%{keyword}%"
    c.execute(query, (like_kw, like_kw, like_kw, like_kw, like_kw))
    rows = c.fetchall()
    conn.close()
    return rows

# --- Search box ---
search_query = st.text_input("🔍 Search candidates by name, skill, qualification, or certification")

if search_query:
    resumes = search_resumes(search_query)
else:
    resumes = get_resumes()

# --- Candidate Ranking by JD ---
st.subheader("📄 Candidate Ranking by Job Description")
jd_text = st.text_area("Paste a Job Description (JD) here:")

ranked_candidates = []
if jd_text and resumes:
    jd_text_lower = jd_text.lower()

    for r in resumes:
        candidate_id, name, qualifications, skills, soft_skills, experience, certifications = r
        score = 0

        # --- Match technical skills ---
        if skills:
            for skill in skills.split(","):
                if skill.strip().lower() in jd_text_lower:
                    score += 2  # technical skills weighted higher

        # --- Match qualifications ---
        if qualifications and any(q in jd_text_lower for q in qualifications.lower().split(",")):
            score += 1

        # --- Match certifications ---
        if certifications and any(cert.lower() in jd_text_lower for cert in certifications.split(",")):
            score += 1

        # --- Match soft skills ---
        if soft_skills and any(s.strip().lower() in jd_text_lower for s in soft_skills.split(",")):
            score += 0.5

        ranked_candidates.append((score, r))

    # Sort by score (higher = better fit)
    ranked_candidates.sort(reverse=True, key=lambda x: x[0])

# --- Display results ---
if resumes:
    if jd_text:
        st.write(f"🏆 Ranked {len(ranked_candidates)} candidate(s) based on JD")
        for score, r in ranked_candidates:
            st.markdown("---")
            st.subheader(f"👤 {r[1]} (ID: {r[0]}) — ⭐ Score: {score}")
            st.markdown(f"**🎓 Qualifications:** {r[2]}")
            st.markdown(f"**🛠 Technical Skills:** {r[3]}")
            st.markdown(f"**🤝 Soft Skills:** {r[4]}")
            st.markdown(f"**⌛ Experience:** {r[5]} years")
            st.markdown(f"**🏅 Certifications:** {r[6]}")
    else:
        st.write(f"Found {len(resumes)} candidate(s).")
        for r in resumes:
            st.markdown("---")
            st.subheader(f"👤 {r[1]} (ID: {r[0]})")
            st.markdown(f"**🎓 Qualifications:** {r[2]}")
            st.markdown(f"**🛠 Technical Skills:** {r[3]}")
            st.markdown(f"**🤝 Soft Skills:** {r[4]}")
            st.markdown(f"**⌛ Experience:** {r[5]} years")
            st.markdown(f"**🏅 Certifications:** {r[6]}")
else:
    st.warning("No resumes found in the database.")
