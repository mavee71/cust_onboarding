import streamlit as st
from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Pinecone client
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=PINECONE_API_KEY)
assistant = pc.assistant.Assistant(assistant_name="customer-onboard")

# Streamlit app layout
st.title("Oracle ERP FCS Customer Onboarding Assistant")
st.write("Interact with the assistant to obtain information about the onboarding process:")

# User input
user_input = st.text_input("Ask your question and click submit:")

if st.button("Submit"):
    if user_input:
        # Create a message object
        user_message = Message(role="user", content=user_input)

        # Send message to assistant
        response = assistant.chat(messages=[user_message])

        # Display assistant's response
        assistant_response = response['message']['content']
        st.write("**Assistant's Response:**")
        st.write(assistant_response)
    else:
        st.error("Please enter a question.")


