import streamlit as st
from components import render_header, render_footer
render_header()
# Back button
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("🤝 Mentor Connect")
st.write("Find and connect with mentors to guide your career path.")

# Sample mentor data
mentors = [
    {"name": "Dr. Anita Sharma", "role": "Data Scientist", "skills": ["Python", "Machine Learning"], "industry": "IT", "contact": "anita@example.com"},
    {"name": "Rajesh Kumar", "role": "Project Manager", "skills": ["Leadership", "Agile", "Scrum"], "industry": "Management", "contact": "rajesh@example.com"},
    {"name": "Neha Gupta", "role": "Cloud Engineer", "skills": ["AWS", "Azure", "DevOps"], "industry": "Cloud", "contact": "neha@example.com"},
]

# Filters
industry_filter = st.selectbox("Filter by Industry", ["All"] + list(set([m["industry"] for m in mentors])))
skill_filter = st.text_input("Search by Skill")

# Show mentors
for mentor in mentors:
    if (industry_filter == "All" or mentor["industry"] == industry_filter) and \
       (not skill_filter or any(skill_filter.lower() in s.lower() for s in mentor["skills"])):

        with st.container():
            st.subheader(f"👤 {mentor['name']}")
            st.write(f"**Role:** {mentor['role']}")
            st.write(f"**Industry:** {mentor['industry']}")
            st.write(f"**Skills:** {', '.join(mentor['skills'])}")
            st.write(f"📧 Contact: {mentor['contact']}")
            if st.button(f"Request Mentorship from {mentor['name']}", key=mentor['name']):
                st.success(f"✅ Request sent to {mentor['name']}! They will contact you soon.")
            render_footer() 