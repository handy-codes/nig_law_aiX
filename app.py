import streamlit as st
from modules.chat_assistant import chat_interface
from modules.document_reviewer import document_review_ui
# from modules.voice_to_text import voice_to_text_ui
from modules.legal_template import template_builder_ui
from modules.law_search import law_search_ui
from modules.query_builder import query_builder_ui

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Naija Legal AI Assistant", layout="wide")
st.title("Nigeria's no. 1 Legal AI Platform")

# -------------------- LOGIN GATE --------------------
# def login():
#     st.markdown("### 🔒 Enter Access Password")
#     password = st.text_input("Password", type="password")
#     if password != "letmein":  # Change this to your actual secret
#         st.stop()

# login()

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚖️ Features")
selection = st.sidebar.radio("Select a tool:", [
    "📜 Document Review",
    "💬 AI Chat Assistant",
    # "🎤 Voice to Text",
    "📝 Legal Template Builder",
    "🔍 Legal Law Search",
    "📂 AI Query Panel"
])

# -------------------- TOOL ROUTER --------------------
if selection == "📜 Document Review":
    document_review_ui()
elif selection == "💬 AI Chat Assistant":
    chat_interface()
# elif selection == "🎤 Voice to Text":
#     voice_to_text_ui()
elif selection == "📝 Legal Template Builder":
    template_builder_ui()
elif selection == "🔍 Legal Law Search":
    law_search_ui()
elif selection == "📂 AI Query Panel":
    query_builder_ui()



# -------------------- SIDEBAR FOOTER WITH BETA LABEL --------------------
st.sidebar.markdown("""<br><br><br><br><br><br><br>""", unsafe_allow_html=True)  # Push down

st.sidebar.markdown(
    '<p style="font-size: 17px; text-align: center; color: #47D1FD;"><em>Beta Release</em></p>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <hr style="margin-top: 0; margin-bottom: 5px;">
    <p style="font-size: 15px; text-align: center;">
        © <a href="https://www.techxos.com" target="_blank" style="text-decoration: none; color: white;">
        Techxos Digital Solutions 2025</a>
    </p>
    """,
    unsafe_allow_html=True
)


# # -------------------- SIDEBAR FOOTER --------------------
# st.sidebar.markdown("""---""")
# st.sidebar.markdown(
#     '<p style="font-size: 15px; ">'
#     '© <a href="https://www.techxos.com" target="_blank" style="text-decoration: none; color: white;">'
#     'Techxos Digital Solutions 2025</a></p>',
#     unsafe_allow_html=True
# )

# -------------------- CUSTOM CSS --------------------
custom_css = """
<style>
    /* Hide default Streamlit footer */
    footer {visibility: hidden;}

    /* Make sidebar toggler larger */
    [data-testid="collapsedControl"] {
        transform: scale(1.5);
        margin-top: 10px;
        margin-left: 8px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)





# # FILE: app.py
# import streamlit as st
# from modules.chat_assistant import chat_interface
# from modules.document_reviewer import document_review_ui
# # from modules.voice_to_text import voice_to_text_ui
# from modules.legal_template import template_builder_ui
# from modules.law_search import law_search_ui
# from modules.query_builder import query_builder_ui

# st.set_page_config(page_title="Naija Legal AI Assistant", layout="wide")
# st.title("Nigeria's No. 1 Legal AI Platform")

# st.sidebar.title("⚖️ Features")
# selection = st.sidebar.radio("Select a tool:", [
#     "📜 Document Review",
#     "💬 AI Chat Assistant",
#     # "🎤 Voice to Text",
#     "📝 Legal Template Builder",
#     "🔍 Legal Law Search",
#     "📂 AI Query Panel"
# ])

# if selection == "📜 Document Review":
#     document_review_ui()
# elif selection == "💬 AI Chat Assistant":
#     chat_interface()
# # elif selection == "🎤 Voice to Text":
# #     voice_to_text_ui()
# elif selection == "📝 Legal Template Builder":
#     template_builder_ui()
# elif selection == "🔍 Legal Law Search":
#     law_search_ui()
# elif selection == "📂 AI Query Panel":
#     query_builder_ui()

# # You'll create each of these modules in the `modules/` folder.

# # .env file should include:
# # GROQ_API_KEY=your_groq_api_key_here



# # # FILE: app.py
# # import streamlit as st
# # from modules.chat_assistant import chat_interface
# # from modules.document_reviewer import document_review_ui
# # from modules.voice_to_text import voice_to_text_ui
# # from modules.legal_template import template_builder_ui
# # from modules.law_search import law_search_ui
# # from modules.query_builder import query_builder_ui

# # st.set_page_config(page_title="Naija Legal AI Assistant", layout="wide")
# # st.title("🇳🇬 Naija Legal AI Platform")

# # st.sidebar.title("⚖️ Features")
# # selection = st.sidebar.radio("Select a tool:", [
# #     "📜 Document Review",
# #     "💬 AI Chat Assistant",
# #     "🎤 Voice to Text",
# #     "📝 Legal Template Builder",
# #     "🔍 Legal Law Search",
# #     "📂 AI Query Panel"
# # ])

# # if selection == "📜 Document Review":
# #     document_review_ui()
# # elif selection == "💬 AI Chat Assistant":
# #     chat_interface()
# # elif selection == "🎤 Voice to Text":
# #     voice_to_text_ui()
# # elif selection == "📝 Legal Template Builder":
# #     template_builder_ui()
# # elif selection == "🔍 Legal Law Search":
# #     law_search_ui()
# # elif selection == "📂 AI Query Panel":
# #     query_builder_ui()

# # # You'll create each of these modules in the `modules/` folder.

# # # .env file should include:
# # # OPENAI_API_KEY=your_openai_key_here
