import streamlit as st
from components import render_header, render_footer

render_header()

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("📊 Skill Gap Analyzer")
st.write("Compare your skills with job requirements and find gaps.")
render_footer()