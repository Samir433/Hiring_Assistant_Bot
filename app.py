import os
import streamlit as st
from groq import Groq
import re
from dotenv import load_dotenv
load_dotenv()
# sma
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
st.title("Hiring Assistant Chatbot")

if "page" not in st.session_state:
    st.session_state.page = "info"

if st.session_state.page == "info":
    st.subheader("Candidate Information")
    name = st.text_input("Enter your full name:")
    email = st.text_input("Enter your email address:")
    mobile_number = st.text_input("Enter your mobile number:")
    location = st.text_input("Enter your current location:")

    experience_options = [
        "0 to 1 year",
        "1 to 3 years",
        "3 to 5 years",
        "5 to 9 years",
        "9+ years"
    ]
    selected_experience = st.selectbox("Select your years of experience:", experience_options)

    position_options = [
        "Software Developer Intern",
        "Data Science Intern",
        "AI/ML Intern",
        "Software Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Frontend Developer",
        "Backend Developer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Full Stack Developer",
        "Data Analyst"
    ]
    selected_position = st.selectbox("Select your desired position:", position_options)

    tech_stack_options = [
        "Python", "Java", "JavaScript", "C++", "C#", "Go", "Ruby",
        "HTML/CSS", "React.js", "Node.js", "Angular", "Vue.js",
        "Django", "Flask", "Spring Boot", "TensorFlow", "PyTorch",
        "SQL", "MongoDB", "PostgreSQL", "Redis", "AWS", "GCP",
        "Langchain", "MySQL", "Data Structures and Algorithms",
        "Azure", "Docker", "Kubernetes", "Git", "Linux", "Pandas",
        "Power BI", "Tableau"
    ]
    selected_tech_stack = st.multiselect("Select your tech stack (maximum 6):", tech_stack_options)

    if st.button("Submit Information"):
        # Validate input fields
        if not name.strip():
            st.error("Please enter your full name.")
        elif not email.strip() or "@" not in email:
            st.error("Please enter a valid email address.")
        elif not mobile_number.strip() or not mobile_number.isdigit() or len(mobile_number) != 10:
            st.error("Please enter a valid 10-digit mobile number.")
        elif not location.strip():
            st.error("Please enter your current location.")
        elif len(selected_tech_stack) > 6:
            st.error("Please select a maximum of 6 technologies.")
        else:
            # Store information in session state
            st.session_state.candidate_info = {
                "name": name,
                "email": email,
                "mobile_number": mobile_number,
                "location": location,
                "experience": selected_experience,
                "position": selected_position,
                "tech_stack": selected_tech_stack,
            }

            st.session_state.page = "questions"
            st.experimental_rerun()

if st.session_state.page == "questions":
    st.subheader("Interview Questions")

    if "questions" not in st.session_state:
        candidate_info = st.session_state.candidate_info
        prompt = f"""
        Generate 5 technical interview questions for a {candidate_info['position']} role with {candidate_info['experience']} of experience. 
        The questions should focus on the following technologies: {', '.join(candidate_info['tech_stack'])}.
        - For less than 1 year experience: Focus on foundational concepts and basic implementation.
        - For 1-3 years: Include intermediate-level design and implementation details.
        - For 3+ years: Focus on advanced problem-solving, optimization, and system design.
        Format:
        1. <Question 1>
        2. <Question 2>
        ...
        """
        try:
            llm_response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful AI Assistant specialized in generating interview questions."},
                    {"role": "user", "content": prompt},
                ],
                model="llama-3.3-70b-versatile",
            )

            generated_text = llm_response.choices[0].message.content
            question_pattern = r"^\d+\.\s*(.*)"
            questions = re.findall(question_pattern, generated_text, re.MULTILINE)

            st.session_state.questions = questions
            st.session_state.answers = [""] * len(questions)
            st.session_state.current_question_index = 0

        except Exception as e:
            st.error(f"Failed to generate questions: {str(e)}")

    if st.session_state.current_question_index < len(st.session_state.questions):
        question = st.session_state.questions[st.session_state.current_question_index]

        st.write(f"### Question {st.session_state.current_question_index + 1}:")
        st.write(question)

        answer = st.text_area(
            "Write your answer:", 
            st.session_state.answers[st.session_state.current_question_index]
        )

        if st.button("Save Answer"):
            st.session_state.answers[st.session_state.current_question_index] = answer
            st.success("Answer saved!")

        if st.button("Next Question"):
            st.session_state.current_question_index += 1
            st.experimental_rerun()

    else:
        st.write("### All questions have been displayed.")
        st.write("Review your answers below:")
        for i, (q, a) in enumerate(zip(st.session_state.questions, st.session_state.answers), 1):
            st.write(f"**Q{i}:** {q}")
            st.write(f"**Your Answer:** {a}")
