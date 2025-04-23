import streamlit as st
from mistralai import Mistral


api_key = st.sidebar.text_input("Enter your Mistral API key")
client = Mistral(api_key=api_key)
# 55k9IsfTgwbYwcSz0DFuHd6u5iJmi9uC

st.title("Echo Bot")


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


    chat_response = client.chat.complete(
        model="ft:open-mistral-7b:cf990a21:20250423:university_KD:5f1235ad",
        messages=st.session_state.messages
       # messages = [{"role":'user', "content": prompt}]
    )
    
    response = chat_response.choices[0].message.content

    response = f"Echo: {response}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})