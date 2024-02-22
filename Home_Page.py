import streamlit as st

# Set page layout and title
st.set_page_config(layout="wide", page_title="Multimedia Chat GPT", page_icon="images/multimedia.png")

# Create a container for the application
with st.container():
    # Display a title for the application
    st.title(" :rainbow[Multimedia Chat GPT] ")
    st.subheader('The  :violet[*Multimedia Chat GPT*]  project is focused on creating an interactive application using Streamlit. The goal is to offer users a platform where they can engage in conversations while interacting with various types of multimedia content. This application aims to provide a seamless experience, allowing individuals to interact with PDF documents, websites, images, and YouTube videos all within a chat interface. With a user-friendly interface, users can easily navigate through different forms of media while conversing, enhancing their overall experience and interaction with the conten')
    
    # Create a divider to separate the header from the grid
    st.divider()
    
    # Create a grid with four columns
    col1, col2, col3, col4 = st.columns(4)
    
    # Add a header and image to the first column
    with col1:
        st.header(":blue[Chat with PDF]")
        st.image('images/pdf.png')
        st.markdown('The *"Chat with PDF"*  application stands out by transforming static PDF documents into dynamic, interactive sessions where users can efficiently extract and engage with information. Where quick and interactive access to document content is beneficial.')
    
    # Add a header and image to the second column
    with col2:
        st.header(":blue[Chat with Website]")
        st.image('images/website.png')
        st.markdown('The *"Chat with Website"* application developed to represents a leap forward in making websites more interactive and user-friendly. By leveraging the power of AI and to can create sophisticated chat interfaces that enhance user engagement.')
    
    # Add a header and image to the third column
    with col3:
        st.header(":blue[Chat with Images]")
        st.image('images/image.png')
        st.markdown('The *"Chat with Images"* application represents a significant step forward in combining the ease of text-based chatting with the expressive power of image sharing. Its simplicity, combined with the depth of interaction and image-enhanced conversations.')
    
    # Add a header and image to the fourth column
    with col4:
        st.header(":blue[Chat with YouTube]")
        st.image('images/youtube.png')
        st.markdown('The *"Chat with YouTube"* application offers users a seamless platform to engage in real-time conversations with YouTube videos. Through this, users can select any YouTube video of their choice and initiate a chat session and share insights alongside it. ')
    
    # Add a divider to separate the grid from the caption
    st.divider()
    
    # Add a caption to explain the application's purpose
    st.caption('This application is particularly useful for educational purposes, research, or any scenario in which quick and interactive access to multimedia content is imperative. Using its interactive features, this user-friendly application empowers users to leverage information effectively across a wide range of disciplines through navigation and analysis of complex data.')
