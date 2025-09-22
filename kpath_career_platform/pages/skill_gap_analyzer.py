import streamlit as st

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("📊 Skill Gap Analyzer")
st.write("Compare your skills with job requirements and find gaps.")
