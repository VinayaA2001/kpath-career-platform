import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            qualifications TEXT,
            skills TEXT,
            soft_skills TEXT,
            experience INTEGER,
            certifications TEXT
        )
    """)
    conn.commit()
    return conn

def save_resume(conn, name, resume_info):
    c = conn.cursor()
    c.execute("""
        INSERT INTO resumes (name, qualifications, skills, soft_skills, experience, certifications)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        ", ".join(resume_info["qualifications"]),
        ", ".join(resume_info["tech_skills"]),
        ", ".join(resume_info["soft_skills"]),
        resume_info["experience"],
        ", ".join(resume_info["certifications"])
    ))
    conn.commit()
