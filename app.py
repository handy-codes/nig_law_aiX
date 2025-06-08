# FILE: app.py
import streamlit as st
from modules.chat_assistant import chat_interface
from modules.document_reviewer import document_review_ui
from modules.voice_to_text import voice_input_ui
from modules.legal_templates import template_builder_ui
from modules.law_search import law_search_ui
from modules.query_builder import query_builder_ui

st.set_page_config(page_title="Naija Legal AI Assistant", layout="wide")
st.title("🇳🇬 Naija Legal AI Platform")

st.sidebar.title("⚖️ Features")
selection = st.sidebar.radio("Select a tool:", [
    "📜 Document Review",
    "💬 AI Chat Assistant",
    "🎤 Voice to Text",
    "📝 Legal Template Builder",
    "🔍 Legal Law Search",
    "📂 AI Query Panel"
])

if selection == "📜 Document Review":
    document_review_ui()
elif selection == "💬 AI Chat Assistant":
    chat_interface()
elif selection == "🎤 Voice to Text":
    voice_input_ui()
elif selection == "📝 Legal Template Builder":
    template_builder_ui()
elif selection == "🔍 Legal Law Search":
    law_search_ui()
elif selection == "📂 AI Query Panel":
    query_builder_ui()

# You’ll create each of these modules in the `modules/` folder.

# .env file should include:
# OPENAI_API_KEY=your_openai_key_here
