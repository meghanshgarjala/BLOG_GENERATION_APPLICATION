from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Ensure the API key is loaded
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

# Initialize Google Gen AI (Vertex AI)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)

# Streamlit app configuration
st.set_page_config(layout="wide", page_title="BlogCraft AI", page_icon="✍️")

# Add custom CSS for styling
custom_css = """
<style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        color: #fff;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        color: #ffffff;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    .stSidebar {
        background-color: #333;
        color: #fff;
        padding: 1rem;
    }
    .stButton > button {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: #fff;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #2575fc, #6a11cb);
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Page title
st.title("📝 BlogCraft AI: Your Ultimate Blogging Partner 🚀")
st.subheader("✨ Craft perfect, engaging blogs effortlessly with the power of AI. Let BlogCraft be your creative companion! 🌟")

# Sidebar for inputs
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter the details of the blog that you want to generate")
    blog_title = st.text_input("Blog Title")
    keywords = st.text_input("Keywords (comma-separated)")
    num_words = st.slider("Number of Words", min_value=200, max_value=2000, step=200)
    submit_button = st.button("Generate Blog ✍️")

# Main content
if submit_button:
    # Ensure input values are provided
    if not blog_title or not keywords:
        st.error("Please provide both a blog title and keywords.")
    else:
        # Create the prompt
        prompt = (
            f"Generate a comprehensive, engaging blog post relevant to the given title "
            f'"{blog_title}" and keywords "{keywords}". Make sure to incorporate these keywords '
            f"in the blog post. The blog should be approximately {num_words} words in length, "
            f"suitable for an online audience. Ensure that the content is original, informative, "
            f"and maintains a consistent tone throughout."
        )

        # Generate blog content
        try:
            with st.spinner("Crafting your blog... ✨"):
                response = llm.predict(prompt)  # Generate content using the AI
            st.success("Your blog has been generated! 🎉")
            st.write(response)
        except Exception as e:
            st.error(f"Error generating blog: {e}")
