# Hiring Assistant Chatbot

A streamlined and efficient chatbot for assisting with technical interview preparation. This application generates customized interview questions based on the candidate's role, experience, and tech stack, while also collecting user responses in an organized format.  

**Deployed on Azure for production-level use**, ensuring scalability, reliability, and security for handling real-world traffic and user data.

---

## Features

1. **Candidate Information Collection**:
   - Collects user details including name, email, phone number, location, experience, and desired position.
   - Allows selection of up to 6 technologies from a predefined tech stack.

2. **Dynamic Question Generation**:
   - Generates tailored interview questions using advanced AI (Llama-3.3-70b model).
   - Adapts questions to the candidate's experience level:
     - **0 to 1 year**: Focus on basic concepts and implementation.
     - **1 to 3 years**: Includes intermediate-level questions.
     - **3+ years**: Focuses on advanced problem-solving and system design.

3. **Answer Recording**:
   - Provides an interface for candidates to write and save answers for each question.
   - Displays a summary of all responses for review before submission.

4. **Submission Confirmation**:
   - Includes plagiarism warning to ensure originality.
   - Provides a clean interface to view all submitted responses.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Samir433/Hiring_Assistant_Bot.git
   ```
    ```bash
   cd hiring-assistant-chatbot
   ```
2. Install Dependencies and Set Up Environment
   ```bash
   pip install -r requirements.txt
   ```
    ```bash
   create .env and set GROQ_API_KEY=your_groq_api_key_here
   ```
3. Run the Application
   ```bash
   streamlit run chatbot.py
   ```

  

