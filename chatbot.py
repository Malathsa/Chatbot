import json
import streamlit as st
from difflib import get_close_matches

def load_data():
    file_path = 'qa_data.json'  
    with open(file_path, 'r') as file:
        return json.load(file)
     
def find_answer(question, data):
    question = question.lower()  
    if question in data:
        return data[question]
  
    similar_questions = get_close_matches(question, data.keys(), n=1, cutoff=0.6)
    if similar_questions:
        return f"Did you mean: {similar_questions[0]}?\nAnswer: {data[similar_questions[0]]}"
    return "Sorry, I don't have an answer for that."

def chatbot():
    st.markdown("<h1 style='color:red;'>PYTHON CHATBOT</h1>", unsafe_allow_html=True)

    st.write("""
    Welcome to PyBetter! 

    I'm here to help you with all things Python. Whether you have coding questions, need tips on libraries, or want to brainstorm project ideas, just ask away! Let’s code something amazing together!
    """)

    data = load_data()
    
    user_input = st.text_input("You: ", "")
    
    if user_input:  
        response = find_answer(user_input, data)
        st.markdown(f"""
        <div style='background-color: transparent; padding: 10px; border-radius: 5px; font-size: 16px; color: white; border: 2px solid white;'>
            {response}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)  
    if st.button('Exit'):
        st.write("Goodbye!")
        st.stop() 


if __name__ == "__main__":
    chatbot()
