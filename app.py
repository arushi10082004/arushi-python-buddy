import streamlit as st
import google.generativeai as genai

# Configure API Key (Best practice: use st.secrets for security, but keeping yours here for now)
genai.configure(api_key="AIzaSyDCwkbBNxflGZiDz5i6DD66FQFtHBCl_FI")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Python AI Learning Buddy Arushi", page_icon="💡")
st.title("💡 Python AI Learning Buddy Arushi")

topic = st.text_input("Enter a topic")
option = st.selectbox(
    "Choose your Activity",
    ["Explain concept", "Real-life example", "Generate quiz", "Ask anything"]
)

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        if option == "Explain concept":
            prompt = f"You are Arushi. Explain the python programming topic '{topic}' in simple language as if teaching a 15-year-old student. Use easy words, one clear analogy, and keep it short."
        elif option == "Real-life example":
            prompt = f"You are Arushi, a friendly Python tutor. Give one real-life example that explains how Python programming topic '{topic}' works. Instructions: Use a situation from everyday life, explain how it relates to Python step by step, use simple language suitable for beginners, keep the explanation under 200 words, and end with one interesting fact about Python."
        elif option == "Generate quiz":
            prompt = f"Generate a 5-multiple choice question quiz on python programming topic '{topic}'. Each question should have 4 options (a, b, c, d) aligned on new lines. After each question, provide the correct answer and a short explanation."
        else:
            prompt = topic
        
        response = model.generate_content(prompt)
        st.write(response.text)
