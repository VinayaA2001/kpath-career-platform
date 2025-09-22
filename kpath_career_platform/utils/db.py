import sqlite3

DB_NAME = "resumes.db"

def get_connection():
    """Get a new database connection"""
    return sqlite3.connect(DB_NAME)

def init_db():
    """Initialize the resumes database and create table if not exists"""
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            qualifications TEXT,
            skills TEXT,
            soft_skills TEXT,
            experience INTEGER,
            certifications TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Database initialized")

def save_resume(name: str, resume_info: dict):
    """Save parsed resume information into the database"""
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO resumes (name, qualifications, skills, soft_skills, experience, certifications)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        name,
        ", ".join(resume_info.get("qualifications", [])),
        ", ".join(resume_info.get("tech_skills", [])),
        ", ".join(resume_info.get("soft_skills", [])),
        resume_info.get("experience", 0),
        ", ".join(resume_info.get("certifications", []))
    ))
    conn.commit()
    conn.close()
    print(f"💾 Resume saved for {name}")

def delete_candidate(candidate_id: int):
    """Delete candidate from database by ID"""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM resumes WHERE id=?", (candidate_id,))
    conn.commit()
    conn.close()
    print(f"🗑 Candidate {candidate_id} deleted")

def fetch_all_resumes():
    """Fetch all resumes from database"""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM resumes")
    rows = c.fetchall()
    conn.close()
    return rows
