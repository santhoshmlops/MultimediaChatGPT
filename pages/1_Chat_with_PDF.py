# Import necessary libraries
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
from utils import load_config


# Load configuration variables
config=load_config()
# Load environment variables 
load_dotenv()
# Configure the GenerativeAI API with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# Function to extract text from PDF files
def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=config['pdf_model']['chunk_size'], 
                                                   chunk_overlap=config['pdf_model']['chunk_overlap'])
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create vector store from text chunks
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model=config['pdf_model']['embedding'])
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Function to load conversational chain for question answering
def get_conversational_chain():
    prompt_template = """
    You are a wonderful assistant who has a great understanding of pdf documents and has advanced search functionalities. A pdf file will be uploaded. Please answer the question as clearly as possible from the provided context.
    If the answer is not available in the context, simply say, "Answer is not available in the PDF"; please don't provide the wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model=config['pdf_model']['model'], 
                                   temperature=config['pdf_model']['temperature'])
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Function to handle user input and generate response
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model=config['pdf_model']['embedding'])
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()   
    response = chain.invoke(
        {"input_documents":docs, "question": user_question},
        return_only_outputs=True
    )   
    return response["output_text"]

# Main function for Streamlit app
def main():
    # Set Streamlit page configuration
    st.set_page_config(page_title="Chat with PDF",page_icon="images\chatbot.png")
    
    # Display title and description
    st.title(":red[Chat with PDF]")
    st.caption("Our project aims to simplify document interactions by integrating Google Gemini Pro with advanced search functionalities that allow users to quickly locate specific documents and conversations within the chat interface.")

    # Allow the user to upload an r PDF files
    pdf_docs = st.file_uploader("Upload your PDF Files ", accept_multiple_files=True)    

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

        with st.spinner("Generating answer..."):
            # Extract text from PDFs and create vector store
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)          
            # Get response to user question
            response = user_input(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):        
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(response) 
        
          


if __name__ == "__main__":
    main()