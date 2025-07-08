import streamlit as st
import requests

# Set the API URL and headers
API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b-it"
headers = {"Authorization": ""}


# Function to query the model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# Streamlit app title
st.title("Hugging Face Model Query App")

# Input text area for user prompt
user_input = st.text_area("Enter your prompt:", height=100)

# Button to submit the query
if st.button("Get Response"):
    if user_input:
        # Query the model with user input
        output = query({"inputs": user_input})

        # Display the generated text in the Streamlit app
        if 'generated_text' in output[0]:
            st.subheader("Model Response:")
            st.markdown(output[0]['generated_text'])
        else:
            st.error("Error: No response generated. Please try again.")
    else:
        st.warning("Please enter a prompt before submitting.")