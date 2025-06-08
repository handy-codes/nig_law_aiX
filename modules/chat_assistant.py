# FILE: modules/chat_assistant.py
import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def chat_interface():
    st.header("💬 Nigerian Legal AI Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "system",
                "content": "You are a legal assistant specialized in Nigerian laws. Answer questions based only on Nigerian legal context."
            }
        ]

    user_input = st.text_input("Ask a legal question (e.g., What are the rights of tenants under the Land Use Act?)")

    if st.button("Ask") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("Thinking like a lawyer..."):
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}"
            }
            payload = {
                "model": "llama3-8b-8192",
                "messages": st.session_state.chat_history,
                "temperature": 0.2,
                "max_tokens": 300,
                "stream": False
            }

            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                st.error(f"API error: {response.status_code} - {response.text}")
                return

            data = response.json()
            answer = data['choices'][0]['message']['content']

            st.session_state.chat_history.append({"role": "assistant", "content": answer})

    for msg in st.session_state.chat_history[1:]:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**LegalBot:** {msg['content']}")




# # FILE: modules/chat_assistant.py
# import streamlit as st
# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def chat_interface():
#     st.header("💬 Nigerian Legal AI Assistant")

#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = [
#             {"role": "system", "content": "You are a legal assistant specialized in Nigerian laws. Answer questions based only on Nigerian legal context."}
#         ]

#     user_input = st.text_input("Ask a legal question (e.g., What are the rights of tenants under the Land Use Act?)")

#     if st.button("Ask") and user_input:
#         st.session_state.chat_history.append({"role": "user", "content": user_input})

#         with st.spinner("Thinking like a lawyer..."):
#             response = openai.ChatCompletion.create(
#                 model="llama3-8b-8192",
#                 messages=st.session_state.chat_history,
#                 temperature=0.2
#             )
#             answer = response.choices[0].message.content
#             st.session_state.chat_history.append({"role": "assistant", "content": answer})

#     for msg in st.session_state.chat_history[1:]:
#         if msg["role"] == "user":
#             st.markdown(f"**You:** {msg['content']}")
#         else:
#             st.markdown(f"**LegalBot:** {msg['content']}")
