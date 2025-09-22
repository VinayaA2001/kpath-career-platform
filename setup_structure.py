import os

structure = {
    "pages": [
        "home.py",
        "career_matchmaking.py",
        "skill_gap_analyzer.py",
        "resume_interview_coach.py",
        "mentor_connect.py",
        "jobs.py",
    ],
    "models": [
        "resume_parser.py",
        "job_matcher.py",
        "skill_recommender.py",
        "interview_ai.py",
    ],
    "utils": [
        "preprocessing.py",
        "db.py",
        "api_integration.py",
    ],
    "data": [],
}

base = "kpath_career_platform"

# Create base folder
os.makedirs(base, exist_ok=True)

# Create subfolders and files
for folder, files in structure.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    for file in files:
        open(os.path.join(path, file), "w").close()

# Create main files
for main_file in ["app.py", "requirements.txt", "README.md"]:
    open(os.path.join(base, main_file), "w").close()

print("✅ Folder structure created successfully!")
