import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")

# Set up OpenAI chat model
chat = ChatOpenAI(api_key=api_key, temperature=0.5)

# Streamlit UI configuration
st.title("💬 ChatSarcastic")
st.caption("🚀 A Streamlit chatbot powered by Langchain 🦜🔗 OpenAI")

# Initialize conversation flow in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
    SystemMessage(content="I am sarcastic comedian")
    ]

# Display chat messages from session state
for msg in st.session_state.messages:
    if isinstance(msg, AIMessage):
        role = "assistant" 
    elif isinstance(msg, SystemMessage):
        role="assistant" 
    else:
        role="user"
    st.chat_message(role).write(msg.content)

# Handle user input and generate responses
if prompt := st.chat_input():
    user_message = HumanMessage(content=prompt)
    st.session_state["messages"].append(user_message)
    st.chat_message("user").write(prompt)

    # Generate AI response
    ai_response = chat(st.session_state["messages"])
    ai_message = AIMessage(content=ai_response.content)
    st.session_state["messages"].append(ai_message)
    st.chat_message("assistant").write(ai_response.content)