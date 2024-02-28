# Import necessary libraries
import os 
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from utils import load_config


# Load configuration variables
config=load_config()
# Load environment variables from .env file
load_dotenv()
# Configure the GenerativeAI API with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Initialize the Generative Model
model = genai.GenerativeModel(config['image_model']['model'])


# Function to process the uploaded image file
def input_image(upload_file):
    if upload_file is not None:
        # Read the file as bytes
        bytes_data = upload_file.getvalue()
        # Create a dictionary representing the image data
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ] 
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Main function for Streamlit app
def main():
    # Set Streamlit page configuration
    st.set_page_config(page_title="Chat with Images", page_icon="images\chatbot.png")

    # Display title and description
    st.title(":red[Chat with Images]")
    st.caption("Our project aims to enhance the chat experience by using Google Vision API to analyze images. By integrating this tool, we can provide more engaging and informative chats based on the given prompts.")

    # Allow the user to upload an image file
    upload_file = st.file_uploader("Choose an image", accept_multiple_files=False, type=["png", "jpg", "jpeg", "img", "webp"])

    # Display the uploaded image if available
    if upload_file is not None:
        image = Image.open(upload_file)
        # Display the uploaded image with a caption
        st.image(image, caption="Uploaded image", use_column_width=True)


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Enter your Question here"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prompt description
        input_prompt = """
        You are a wonderful assistant who has an excellent understanding of images and can describe them perfectly. A picture will be uploaded, and you will have to answer any questions based on the image. After that, you will need to give a detailed explanation.
        """

        with st.spinner("Generating answer..."):
            image_data = input_image(upload_file)
            # Generate response based on the user input and uploaded image
            response = model.generate_content([input_prompt, image_data[0], prompt])
            # Display the response with a subheader

        # Display assistant response in chat message container
        with st.chat_message("assistant"):        
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.markdown(response.text) 
        


if __name__ == "__main__":
    main()