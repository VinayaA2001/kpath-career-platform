import random

# Role-based interview questions
role_questions = {
    "Data Scientist": [
        "Explain supervised vs unsupervised learning.",
        "How do you handle missing data?",
    ],
    "Software Engineer": [
        "What are OOP principles?",
        "How do you debug a slow SQL query?",
    ],
    "Frontend Developer": [
        "What’s the difference between state and props in React?",
        "How do you improve website performance?",
    ],
    "Backend Developer": [
        "Explain REST vs GraphQL.",
        "How do you secure APIs?",
    ],
    "AI/ML Engineer": [
        "How do you prevent overfitting?",
        "Explain CNNs vs RNNs.",
    ],
    "Business Analyst": [
        "How do you gather requirements?",
        "What tools do you use for visualization?",
    ],
}

def get_questions(role):
    return role_questions.get(role, [])

def evaluate_answer(question, answer):
    """
    Simple scoring logic:
    - Short answers (<15 words) → low score
    - Medium answers (15–40 words) → medium score
    - Long detailed answers (>40 words) → high score
    """
    words = len(answer.split())

    if words < 15:
        score = random.randint(2, 4)
        feedback = "Your answer is too short. Try explaining with more details and examples."
    elif words < 40:
        score = random.randint(5, 7)
        feedback = "Decent answer. You can add more structure (Situation, Task, Action, Result)."
    else:
        score = random.randint(8, 10)
        feedback = "Great answer! Well explained with enough details."

    return score, feedback
