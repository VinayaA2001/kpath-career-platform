import streamlit as st
import sqlite3
from components import render_header, render_footer

render_header()

# --- Database Setup ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT
        )
    """)
    conn.commit()
    return conn

def add_job(title, company, location, description):
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO jobs (title, company, location, description) VALUES (?, ?, ?, ?)",
              (title, company, location, description))
    conn.commit()
    conn.close()

def get_jobs():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT * FROM jobs")
    jobs = c.fetchall()
    conn.close()
    return jobs

def delete_job(job_id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM jobs WHERE id=?", (job_id,))
    conn.commit()
    conn.close()

def update_job(job_id, title, company, location, description):
    conn = init_db()
    c = conn.cursor()
    c.execute("UPDATE jobs SET title=?, company=?, location=?, description=? WHERE id=?",
              (title, company, location, description, job_id))
    conn.commit()
    conn.close()

# --- Streamlit UI ---
st.title("💼 Job Management Dashboard")

st.sidebar.header("➕ Add a New Job")
title = st.sidebar.text_input("Job Title")
company = st.sidebar.text_input("Company")
location = st.sidebar.text_input("Location")
description = st.sidebar.text_area("Job Description")

if st.sidebar.button("Add Job"):
    if title and company and location and description:
        add_job(title, company, location, description)
        st.sidebar.success("✅ Job added successfully!")
        st.rerun()
    else:
        st.sidebar.error("⚠️ Please fill in all fields.")

st.subheader("📋 Job Listings")
jobs = get_jobs()

if jobs:
    for job in jobs:
        job_id, job_title, job_company, job_location, job_desc = job
        with st.expander(f"🔹 {job_title} at {job_company} ({job_location})"):
            st.write(job_desc)

            col1, col2 = st.columns(2)

            # --- Edit Job ---
            with col1:
                if st.button(f"✏️ Edit {job_id}"):
                    with st.form(f"edit_form_{job_id}"):
                        new_title = st.text_input("Job Title", value=job_title)
                        new_company = st.text_input("Company", value=job_company)
                        new_location = st.text_input("Location", value=job_location)
                        new_desc = st.text_area("Job Description", value=job_desc)
                        submit = st.form_submit_button("Save Changes")

                        if submit:
                            update_job(job_id, new_title, new_company, new_location, new_desc)
                            st.success("✅ Job updated successfully!")
                            st.rerun()

            # --- Delete Job ---
            with col2:
                if st.button(f"🗑️ Delete {job_id}"):
                    delete_job(job_id)
                    st.warning("❌ Job deleted.")
                    st.rerun()
else:
    st.info("No jobs available. Please add a new one from the sidebar.")
render_footer()
