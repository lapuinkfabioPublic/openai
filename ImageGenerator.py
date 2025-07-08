import streamlit as st
import requests
import io
from PIL import Image #pip install pillow



# Set the API URL and headers
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": ""}

# Function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit application
st.title("Image Generation with Hugging Face")

# Input for text prompt
prompt = st.text_input("Enter a description for the image (e.g., 'Astronaut riding a horse'):")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            # Query the API with the user's input
            image_bytes = query({"inputs": prompt,
                                 "parameters":
                                     {"width": 1280,
                                      "height": 720}}) # x8 16/9

            # Open the image using PIL
            # print(image_bytes)
            image = Image.open(io.BytesIO(image_bytes))
            image.save("image.jpeg")
            # Display the generated image
            st.image(image, caption=f"Generated Image for: '{prompt}'", use_column_width=True)
    else:
        st.warning("Please enter a description to generate an image.")
