import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        qualifications TEXT,
        skills TEXT,
        soft_skills TEXT,
        experience TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized with resumes table")

if __name__ == "__main__":
    init_db()
