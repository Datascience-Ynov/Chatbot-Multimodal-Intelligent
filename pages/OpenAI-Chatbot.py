import streamlit as st
from openai import OpenAI


api_key = st.sidebar.text_input("Enter your Mistral API key")
client = OpenAI(api_key=api_key)
# 55k9IsfTgwbYwcSz0DFuHd6u5iJmi9uC

st.title("OpenAI Bot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    
    response = chat_response.choices[0].message.content

    response = f"Echo: {response}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})