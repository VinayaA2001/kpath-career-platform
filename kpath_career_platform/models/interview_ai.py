import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Interview AI", page_icon="🤖", layout="wide")

# --- Back Button ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("🤖 AI Interview Coach")

st.write("Practice your interview skills with AI-generated questions and instant feedback.")

# --- Select role ---
role = st.selectbox("Choose the role you're applying for:", 
                    ["Data Scientist", "Software Engineer", "Frontend Developer", "Backend Developer", "AI/ML Engineer", "Business Analyst"])

if role:
    st.subheader(f"💼 Mock Interview for {role}")

    # Example questions
    questions = {
        "Data Scientist": [
            "Can you explain the difference between supervised and unsupervised learning?",
            "How would you handle missing values in a dataset?",
        ],
        "Software Engineer": [
            "What are the main principles of Object-Oriented Programming?",
            "How would you optimize a slow SQL query?",
        ],
        "Frontend Developer": [
            "What’s the difference between React state and props?",
            "How do you improve website performance?",
        ],
        "Backend Developer": [
            "What’s the difference between REST and GraphQL?",
            "How do you secure APIs from unauthorized access?",
        ],
        "AI/ML Engineer": [
            "How do you prevent overfitting in machine learning?",
            "Explain the difference between CNNs and RNNs.",
        ],
        "Business Analyst": [
            "How do you gather requirements from stakeholders?",
            "What tools do you use for data visualization?",
        ],
    }

    for q in questions[role]:
        st.markdown(f"**❓ {q}**")
        answer = st.text_area("Your Answer:", key=q)

        if answer:
            # Simple keyword-based feedback
            if len(answer.split()) < 15:
                st.warning("⚠️ Try to expand your answer with more details.")
            else:
                st.success("✅ Good! You provided a detailed answer.")

st.info("💡 Tip: Use STAR (Situation, Task, Action, Result) method for answering behavioral questions.")
