# Multimedia Chat GPT

## Overview
This project introduces a dynamic Streamlit application designed to facilitate engaging chat interfaces enriched with multimedia content. Leveraging cutting-edge language models from Google, including Gemini Pro and Gemini Pro Vision, our application offers users an interactive platform to communicate effectively while seamlessly integrating various media formats.

## Key Features
1. **Multimedia Integration:** Our application enables users to chat with diverse multimedia content, including PDF documents, websites, images, and YouTube videos.
2. **Google Gemini Pro:** Powered by advanced language models, the application ensures robust and natural language processing capabilities for smooth interaction.
3. **Streamlit Interface:** The user-friendly Streamlit framework provides an intuitive environment for users to navigate and interact with the chat interface effortlessly.

## Objectives
- Enhance communication experiences by offering a versatile platform for interacting with multimedia content.
- Showcase the capabilities of Google Gemini Pro and Gemini Pro Vision in real-world applications.
- Provide a seamless and user-friendly interface for individuals seeking interactive communication solutions.

## Outcomes
- Successful development and deployment of a Streamlit application with integrated multimedia chat capabilities.
- Positive user feedback highlighting the application's ease of use and effectiveness in engaging communication.
- Demonstrated potential for broader applications of language models in enhancing user experiences across various domains.

## Conclusion
Our project marks a significant step forward in the realm of interactive communication, offering a glimpse into the future of multimedia-rich chat interfaces powered by advanced language technologies.

# Project Video
https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/5cb28e4f-e05f-474e-98cf-9aa9b00084d6


# How to Download and Run Project?
### You will need to copy and paste the following code into your terminal :

### STEP 01 - Clone this repository:

```bash
git clone https://github.com/santhoshmlops/MultimediaChatGPT.git
```
```bash
cd MultimediaChatGPT
```

### STEP 02 - Create a conda environment or python environment:

```bash
conda create -n venv python=3.10 -y
```

```bash
conda activate venv
```
or

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### STEP 03 - Install the Requirements : 
```bash
pip install -r requirements.txt
```
### STEP 04 - Create an API key and save it in an environment variable : 

i.  Create your API key by signing in at the following link
```bash
https://makersuite.google.com/app/apikey
```

ii. You will need to rename the .env.example file to .env and then add your API key to the file.

GOOGLE_API_KEY = "Add Your Google API Key Here"

### STEP 05 - Run the Streamlit Application : 
```bash
streamlit run Home_Page.py
```

# Home Page
![Screenshot (157)](https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/879e1848-96d0-438f-bdb4-39402fa1a660)
# Chat with PDF
![Screenshot (151)](https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/80ec618c-d30a-4500-b240-872f7351b590)
# Chat with Website
![Screenshot (153)](https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/b46145a2-9b71-4831-b98a-75ea8e4faa63)
# Chat with Images
![Screenshot (154)](https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/2a7e207c-56e2-4f34-8d13-2cdd1cb3d20f)
# Chat with Youtube
![Screenshot (155)](https://github.com/santhoshmlops/MultimediaChatGPT/assets/133121635/c332bf7c-ec44-49eb-9284-7b861a51b2c5)





