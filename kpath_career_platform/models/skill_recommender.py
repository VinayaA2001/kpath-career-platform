import streamlit as st

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("📚 Skill Recommendation")
st.write("Get personalized skill recommendations to boost your career!")

# Mock roles with required skills
career_skills = {
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Deep Learning", "TensorFlow", "NLP"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "UI/UX"],
    "Cloud Engineer": ["AWS", "Azure", "Docker", "Kubernetes", "CI/CD"],
}

# Input
role = st.selectbox("Select your target career role:", list(career_skills.keys()))
current_skills = st.text_area("Enter your current skills (comma separated):").split(",")

if st.button("🔍 Recommend Skills"):
    current_skills = [s.strip().lower() for s in current_skills]
    missing_skills = [s for s in career_skills[role] if s.lower() not in current_skills]

    st.subheader(f"✨ Recommended Skills for {role}:")
    if missing_skills:
        for skill in missing_skills:
            st.write(f"✅ Learn **{skill}** (Suggested: [Google Search](https://www.google.com/search?q={skill}+course))")
    else:
        st.success("🎉 You already have all the core skills for this role!")
