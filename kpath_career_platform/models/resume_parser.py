import re
import spacy


# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# --- Dictionaries of skills ---
TECH_SKILLS = [
    "python", "java", "c++", "sql", "javascript", "html", "css",
    "machine learning", "deep learning", "nlp", "react", "node.js",
    "cloud", "aws", "azure", "git", "docker", "kubernetes"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving",
    "time management", "adaptability", "creativity", "critical thinking"
]

# --- Extract Years of Experience ---
def extract_years_of_experience(text: str):
    match = re.search(r"(\d+)\+?\s+years?", text.lower())
    if match:
        return int(match.group(1))
    return 0

# --- Extract Resume Info ---
def extract_resume_info(resume_text: str):
    doc = nlp(resume_text)

    qualifications, certifications, orgs = [], [], []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            orgs.append(ent.text)

    for line in resume_text.split("\n"):
        line_lower = line.lower()
        if any(word in line_lower for word in ["b.tech", "bachelor", "master", "mba", "phd", "m.tech", "degree"]):
            qualifications.append(line.strip())
        if "certified" in line_lower or "certificate" in line_lower or "certification" in line_lower:
            certifications.append(line.strip())

    tech_skills = [s for s in TECH_SKILLS if s in resume_text.lower()]
    soft_skills = [s for s in SOFT_SKILLS if s in resume_text.lower()]
    years_exp = extract_years_of_experience(resume_text)

    return {
        "qualifications": list(set(qualifications)),
        "tech_skills": list(set(tech_skills)),
        "soft_skills": list(set(soft_skills)),
        "experience": years_exp,
        "certifications": list(set(certifications)),
        "organizations": list(set(orgs)),
    }

# --- Career Suggestions ---
def suggest_careers(resume_info):
    skills = set(resume_info.get("tech_skills", []))
    soft = set(resume_info.get("soft_skills", []))
    quals = " ".join(resume_info.get("qualifications", [])).lower()

    career_paths = []

    # --- Tech Careers ---
    if {"python", "sql", "machine learning"} & skills:
        career_paths.append("Data Scientist / Machine Learning Engineer")
    if {"python", "sql"} & skills:
        career_paths.append("Data Analyst")
    if {"html", "css", "javascript", "react"} & skills:
        career_paths.append("Frontend Developer")
    if {"node.js", "react", "sql"} & skills:
        career_paths.append("Full Stack Developer")
    if {"java", "c++"} & skills:
        career_paths.append("Software Engineer / Backend Developer")
    if {"aws", "azure", "docker", "kubernetes"} & skills:
        career_paths.append("Cloud / DevOps Engineer")

    # --- Business Careers ---
    if "mba" in quals or "management" in quals:
        career_paths.append("Business Analyst / Management Role")

    # --- Soft skills based ---
    if {"communication", "teamwork"} & soft and "teaching" in quals:
        career_paths.append("Trainer / Educator")
    if {"leadership", "problem solving"} & soft:
        career_paths.append("Project Manager")

    if not career_paths:
        career_paths.append("General Graduate Roles (Trainee, Analyst, Assistant)")

    return list(set(career_paths))
