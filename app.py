import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import (ChatPromptTemplate)
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
groq_api_key=os.getenv('GORQ_API_KEY')



# Genrate blog
def generate_blog(content_type,keywords,tone,word_count,audience):

    # Prompt_template
    prompt_template1 = """
        Generate a {content_type} based on the following keywords: {keywords}.
        The tone of the content should be {tone}.
        The content should be around {word_count} words long and should be suitable for a {audience} audience.
        also it should be in proper structure like title must be bold and generated content below it and then in the end provide 5-10 hags tage to boost content.
    """
    
    chat_template = ChatPromptTemplate.from_messages([
        "system","Your name is Atom and you are a AI-Powered Content Generator and your are expect in this field And give accurate content.",
        "human",prompt_template1
    ])
    model = ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)
    chain = chat_template | model | StrOutputParser()
    response = chain.invoke({"content_type":content_type,"keywords":keywords,"tone":tone,"word_count":word_count,"audience":audience})

    return response




# Streamlit UI Design
st.set_page_config(
    page_title="AtomGPT",
    page_icon="🤖"
)

st.header("AtomGPT 🤖 AI-Powered Content Generator")


with st.sidebar:
    content_type = st.selectbox("Content Type", ["Blog Post", "Article", "Social Media Post"])
    keywords = st.text_input("Enter Keywords to Content Generate (comma-separated)", "Digital Marketing,Ai",)
    tone = st.selectbox("Tone", ["Informal", "Formal", "Persuasive", "Neutral"])
    word_count = st.slider("Word Count", min_value=100, max_value=500, value=100,step=100)
    audience = st.selectbox("Audience", ["General", "Tech Enthusiasts", "Marketers", "Business Professionals","Student"])
    submit = st.button("Generate Blog")
    
    st.title("Create by Krishi Devani")
    st.write("This app allows you to ask questions and get answers based on stored documents.")

    st.header("Tools Uded")
    st.markdown("[Streamlit](https://docs.streamlit.io/)")
    st.markdown("[Langchain](https://github.com/hwchase17/langchain)")
    st.markdown("[Python](https://docs.python.org/3/)")
    st.markdown("[Krishi](https://www.krishidevani.com/)")
if submit:
    response = generate_blog(content_type,keywords,tone,word_count,audience)
    st.markdown(response)




