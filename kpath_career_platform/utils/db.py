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

def delete_candidate(candidate_id: int):
    """Delete candidate from database by ID"""
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM resumes WHERE id=?", (candidate_id,))
    conn.commit()
    conn.close()
