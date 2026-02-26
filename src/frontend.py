import streamlit as st
from PIL import Image
from chain import summarizer



def add_logo(logo_path, width, height):
    logo = Image.open(logo_path)
    modified_logo = logo.resize(width, height)
    return modified_logo


def main():
    # Set page title
    st.set_page_config(page_title="summarizer App", page_icon="-", layout="wide")
    # Set title
    st.title("Summarizer", anchor=False)
    st.header("Summarize Articles using Mistral", anchor=False)
    st.sidebar.image(add_logo("source...", 250, 250))
    st.sidebar.title("Navigation")
    st.sidebar.markdown("- Home")
    st.sidebar.markdown("- About")
    st.sidebar.markdown("- Contact")
    # Input URL
    
