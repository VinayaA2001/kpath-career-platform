import streamlit as st
import sqlite3

st.title("📂 Resume Viewer (Recruiter Mode)")

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
    query = f"""
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

# --- Display resumes ---
if resumes:
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
