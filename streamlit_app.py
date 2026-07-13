import streamlit as st
import requests

API_URL = API_URL = "https://multi-agent-coding-assistant-3v65.onrender.com"

st.set_page_config(
    page_title="AI Coding Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4F46E5;
    }

    .sub-title {
        text-align:center;
        font-size:18px;
        color:gray;
    }

    .stChatMessage {
        border-radius:15px;
    }

    .sidebar-title {
        font-size:22px;
        font-weight:bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Header

st.markdown(
    "<div class='main-title'>🤖 Multi-Agent Coding Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Interview Preparation Assistant powered by LangGraph + Ollama</div>",
    unsafe_allow_html=True
)


st.divider()


# Sidebar

with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'>⚙️ Settings</div>",
        unsafe_allow_html=True
    )

    agent = st.selectbox(
        "Choose Agent",
        [
            "Auto Detect",
            "Java Agent",
            "DSA Agent",
            "SQL Agent",
            "HR Agent"
        ]
    )


    st.write("")


    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()


    st.divider()

    st.info(
        """
        Supported Topics:

        ☕ Java  
        🧩 DSA  
        🗄 SQL  
        💼 HR Interview  
        """
    )


# Chat memory

if "messages" not in st.session_state:

    st.session_state.messages = []


# Display Chat

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



# User input

question = st.chat_input(
    "Ask your interview question..."
)



if question:


    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )


    with st.chat_message("user"):

        st.markdown(question)



    with st.chat_message("assistant"):


        with st.spinner("🤖 Agents are working..."):


            try:

                response = requests.post(

                    API_URL,

                    json={
                        "question": question
                    },

                    timeout=120

                )


                if response.status_code == 200:


                    result = response.json()


                    answer = result.get(
                        "response",
                        "No response generated"
                    )


                    st.markdown(answer)



                    st.session_state.messages.append(

                        {
                            "role":"assistant",
                            "content":answer
                        }

                    )


                else:


                    st.error(
                        f"Server Error : {response.status_code}"
                    )


            except requests.exceptions.ConnectionError:


                st.error(
                    "❌ FastAPI server is not running"
                )


            except Exception as e:


                st.error(
                    f"Error : {str(e)}"
                )