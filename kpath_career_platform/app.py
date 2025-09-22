import streamlit as st
from utils import db

# Initialize DB on app startup
db.init_db()
# --- Page Config ---
st.set_page_config(
    page_title="K-Path Career Platform",
    page_icon="🎓",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1, h2, h3 {
            font-weight: 600;
        }
        .hero {
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(120deg, #2980b9, #6dd5fa, #ffffff);
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
        }
        .hero h1 {
            font-size: 3.2rem;
            margin-bottom: 0.5rem;
        }
        .hero p {
            font-size: 1.25rem;
        }
        .card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            text-align: center;
            transition: all 0.3s ease-in-out;
            height: 100%;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        }
        .card h3 {
            color: #00796b;
        }
        .footer {
            margin-top: 3rem;
            padding: 1.5rem;
            text-align: center;
            background: #004d40;
            color: white;
            border-radius: 12px;
        }
        .footer a {
            color: #ffcc80;
            font-weight: bold;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero">
        <h1>🚀 K-Path Career Platform</h1>
        <p>AI-powered career guidance, interview practice, and recruitment made simple.</p>
    </div>
""", unsafe_allow_html=True)

# --- Features Section ---
st.markdown("## 🌟 Explore the Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='card'>
            <h3>📂 Resume Analyzer</h3>
            <p>Upload resumes to extract skills, experience, and qualifications automatically.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go ➝", key="resume"):
        st.switch_page("pages/resume_analyzer.py")

with col2:
    st.markdown("""
        <div class='card'>
            <h3>🎯 Career Matchmaking</h3>
            <p>Match your resume against job descriptions and identify skill gaps instantly.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go ➝", key="career"):
        st.switch_page("pages/career_matchmaking.py")

with col3:
    st.markdown("""
        <div class='card'>
            <h3>🏢 Recruiter Dashboard</h3>
            <p>Recruiters can search, filter, and find top candidates with AI-powered insights.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go ➝", key="recruiter"):
        st.switch_page("pages/recruiter_dashboard.py")

# --- New Section ---
st.markdown("## 🤖 AI & Job Tools")

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
        <div class='card'>
            <h3>🤖 Interview AI</h3>
            <p>Practice mock interviews with AI-generated questions and feedback.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go ➝", key="interview_ai"):
        st.switch_page("pages/interview_ai.py")

with col5:
    st.markdown("""
        <div class='card'>
            <h3>🔍 Job Matcher</h3>
            <p>Get job recommendations based on your resume and skills.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go ➝", key="job_matcher"):
        st.switch_page("pages/job_matcher.py")

# --- Footer ---
st.markdown("""
    <div class="footer">
        <p>© 2025 K-Path Career Platform | Built with ❤️ using <a href="https://streamlit.io/" target="_blank">Streamlit</a></p>
    </div>
""", unsafe_allow_html=True)
