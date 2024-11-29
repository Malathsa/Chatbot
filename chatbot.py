import json
import streamlit as st
from difflib import get_close_matches

# تحميل قاعدة البيانات من Google Drive
def load_data():
    # تغيير هذا المسار حسب المكان الذي خزنت فيه قاعدة البيانات (على جهازك المحلي)
    file_path = 'qa_data.json'  # تأكد من أن الملف موجود في نفس المجلد أو قدم المسار الصحيح
    with open(file_path, 'r') as file:
        return json.load(file)
     
# البحث عن الإجابة
def find_answer(question, data):
    question = question.lower()  # تحويل السؤال إلى أحرف صغيرة
    if question in data:
        return data[question]
    # البحث عن أقرب سؤال مشابه باستخدام get_close_matches
    similar_questions = get_close_matches(question, data.keys(), n=1, cutoff=0.6)
    if similar_questions:
        return f"Did you mean: {similar_questions[0]}?\nAnswer: {data[similar_questions[0]]}"
    return "Sorry, I don't have an answer for that."

# واجهة المستخدم باستخدام Streamlit
def chatbot():
    st.title("Python Chatbot")
    st.write("Welcome to the Python chatbot! Type 'exit' to quit.")

    data = load_data()
    
    user_input = st.text_input("You: ")
    
    if user_input.lower() == "exit":
        st.write("Goodbye!")
    else:
        response = find_answer(user_input, data)
        st.write(f"Bot: {response}")

# تشغيل البوت
if __name__ == "__main__":
    chatbot()