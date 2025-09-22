import streamlit as st
from models import interview_ai

st.set_page_config(page_title="Mock Interview AI", page_icon="🤖", layout="wide")

# --- Back Button ---
if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.title("🎤 AI Mock Interview Simulator")

st.write("Answer questions one by one, get instant AI feedback, and see your overall score at the end.")

# --- Role Selection ---
role = st.selectbox("Choose your role:", [
    "Data Scientist", 
    "Software Engineer", 
    "Frontend Developer", 
    "Backend Developer", 
    "AI/ML Engineer", 
    "Business Analyst"
])

# Load role-based questions
questions = interview_ai.get_questions(role)

# --- Session State ---
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "scores" not in st.session_state:
    st.session_state.scores = []
if "feedback" not in st.session_state:
    st.session_state.feedback = []

# --- Interview Flow ---
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(f"❓ Question {st.session_state.current_q+1}: {q}")

    answer = st.text_area("💬 Your Answer:", key=f"answer_{st.session_state.current_q}")

    if st.button("Submit Answer"):
        if answer.strip():
            score, feedback = interview_ai.evaluate_answer(q, answer)
            st.session_state.scores.append(score)
            st.session_state.feedback.append((q, feedback, score))
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.warning("⚠️ Please type your answer before submitting.")

else:
    # --- Final Results ---
    st.success("✅ Interview Completed!")

    total_score = sum(st.session_state.scores)
    avg_score = total_score / len(st.session_state.scores)

    st.subheader(f"📊 Final Score: {avg_score:.2f} / 10")

    st.markdown("---")
    st.subheader("📝 Detailed Feedback")
    for i, (q, fb, sc) in enumerate(st.session_state.feedback, start=1):
        st.markdown(f"**Q{i}: {q}**")
        st.write(f"⭐ Score: {sc}/10")
        st.info(fb)

    if st.button("🔄 Restart Interview"):
        st.session_state.current_q = 0
        st.session_state.scores = []
        st.session_state.feedback = []
        st.rerun()
