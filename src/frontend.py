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
    st.divider()
    url = st.text_input("Enter URL of any article", value="")
    # Download audio
    st.divider()
    if url:
        with st.status("Processing...", state="running", expanded=True) as status:
            st.write(" Summarizing Article...")
            summary, time_taken = summarizer(url)
            status.update(label=f"Finished - Time Taken: {time_taken} seconds", state="complete")
            # Show Summary
            st.subheader("Summary:", anchor=False)
            st.write(summary)


   if __name__=="__main__":
    main()


    # For run :python chain.py
    # Then: streamlit run frontend.py
