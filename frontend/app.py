import streamlit as st
import requests

st.set_page_config(page_title="Calendar Bot 🤖", page_icon="🗓️")

st.title("📅 Conversational Calendar Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="user_input")

if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send to backend
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"query": user_input}
        )

        if response.status_code == 200:
            result = response.json().get("response", "No response")
        else:
            result = f"Server Error: {response.status_code}"

    except Exception as e:
        result = f"Client Error: {str(e)}"

    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": result})

# Display chat messages
for msg in st.session_state.messages:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Assistant"
    st.markdown(f"**{role}:** {msg['content']}")
