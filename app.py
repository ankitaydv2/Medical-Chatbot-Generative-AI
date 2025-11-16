import streamlit as st
from src.medical_chat_model import MedicalChatbot

st.set_page_config(page_title="Medibot - Medical Assistant")
st.title("👩‍⚕️ Medibot – AI Medical Chat Assistant")

bot = MedicalChatbot()

user_input = st.text_input("Ask your medical question:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = bot.reply(user_input)
        st.success(answer)
