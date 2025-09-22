import streamlit as st
import sqlite3

# --- Page Config ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")
    
st.set_page_config(page_title="Recruiter Dashboard", page_icon="👔", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .candidate-card {
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: #fafafa;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .candidate-card:hover {
        background-color: #f0f8ff;
        border-color: #007ACC;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.title("👔 Recruiter Dashboard")
st.caption("Search, rank, and evaluate candidates with ease.")

# --- Database Functions ---
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

# --- Sidebar Controls ---
with st.sidebar:
    st.header("🔍 Candidate Search & Ranking")
    search_query = st.text_input("Search by name, skill, qualification, or certification")
    jd_text = st.text_area("📄 Paste a Job Description (JD) here")

# --- Load resumes ---
resumes = search_resumes(search_query) if search_query else get_resumes()

# --- Candidate Ranking ---
ranked_candidates = []
if jd_text and resumes:
    jd_text_lower = jd_text.lower()

    for r in resumes:
        candidate_id, name, qualifications, skills, soft_skills, experience, certifications = r
        score = 0

        if skills:
            for skill in skills.split(","):
                if skill.strip().lower() in jd_text_lower:
                    score += 2
        if qualifications and any(q in jd_text_lower for q in qualifications.lower().split(",")):
            score += 1
        if certifications and any(cert.lower() in jd_text_lower for cert in certifications.split(",")):
            score += 1
        if soft_skills and any(s.strip().lower() in jd_text_lower for s in soft_skills.split(",")):
            score += 0.5

        ranked_candidates.append((score, r))

    ranked_candidates.sort(reverse=True, key=lambda x: x[0])

# --- Display Results ---
if resumes:
    if jd_text:
        st.subheader(f"🏆 Ranked Candidates ({len(ranked_candidates)})")

        for i, (score, r) in enumerate(ranked_candidates, start=1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "⭐"
            with st.container():
                st.markdown(f"""
                <div class="candidate-card">
                    <h4>{medal} {r[1]} (ID: {r[0]}) — ⭐ Score: {score}</h4>
                    <b>🎓 Qualifications:</b> {r[2]}<br>
                    <b>🛠 Technical Skills:</b> {r[3]}<br>
                    <b>🤝 Soft Skills:</b> {r[4]}<br>
                    <b>⌛ Experience:</b> {r[5]} years<br>
                    <b>🏅 Certifications:</b> {r[6]}<br>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.subheader(f"👤 Candidate Profiles ({len(resumes)})")
        for r in resumes:
            with st.container():
                st.markdown(f"""
                <div class="candidate-card">
                    <h4>👤 {r[1]} (ID: {r[0]})</h4>
                    <b>🎓 Qualifications:</b> {r[2]}<br>
                    <b>🛠 Technical Skills:</b> {r[3]}<br>
                    <b>🤝 Soft Skills:</b> {r[4]}<br>
                    <b>⌛ Experience:</b> {r[5]} years<br>
                    <b>🏅 Certifications:</b> {r[6]}<br>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning("⚠️ No resumes found in the database.")
