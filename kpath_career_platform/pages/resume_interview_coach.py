import streamlit as st
from components import render_header, render_footer

render_header()
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("📝 Resume & Interview Coach")
st.write("Get resume tips and practice interview questions for your dream role!")

# Input
role = st.selectbox("Select your target role:", ["Data Scientist", "Frontend Developer", "Cloud Engineer", "Project Manager"])

resume_text = st.text_area("Paste your Resume Text here:")

if st.button("Analyze Resume"):
    st.subheader("📊 Resume Feedback:")
    if "python" not in resume_text.lower() and role == "Data Scientist":
        st.warning("⚠ Your resume is missing Python – a must-have for Data Scientists.")
    if "sql" not in resume_text.lower() and role in ["Data Scientist", "Cloud Engineer"]:
        st.warning("⚠ Add SQL skills to improve ATS score.")
    if "leadership" not in resume_text.lower() and role == "Project Manager":
        st.warning("⚠ Highlight leadership and management achievements.")

    st.success("✅ Resume analysis complete!")

# Mock interview questions
st.subheader("🎤 Practice Interview Questions")
questions = {
    "Data Scientist": [
        "Explain supervised vs. unsupervised learning.",
        "How would you handle imbalanced datasets?",
        "What are precision and recall?"
    ],
    "Frontend Developer": [
        "What are the differences between React and Angular?",
        "Explain the virtual DOM.",
        "How do you optimize a website for performance?"
    ],
    "Cloud Engineer": [
        "What is the difference between AWS EC2 and S3?",
        "Explain Docker vs. Kubernetes.",
        "What is CI/CD?"
    ],
    "Project Manager": [
        "Explain Agile vs. Waterfall methodologies.",
        "How do you handle conflicts in your team?",
        "What’s your experience with project management tools?"
    ]
}

if role:
    st.write("Here are some common interview questions:")
    for q in questions[role]:
        st.write(f"👉 {q}")
render_footer()