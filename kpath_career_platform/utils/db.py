import sqlite3

DB_NAME = "resumes.db"

def init_db():
    """Initialize the resumes database"""
    conn = sqlite3.connect(DB_NAME)
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
    return conn

def delete_candidate(conn, candidate_id):
    """Delete candidate from database by ID"""
    c = conn.cursor()
    c.execute("DELETE FROM resumes WHERE id=?", (candidate_id,))
    conn.commit()
