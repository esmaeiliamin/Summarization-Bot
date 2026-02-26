import streamlit as st
from PIL import Image
from chain import summarizer



def add_logo(logo_path, width, height):
    logo = Image.open(logo_path)
    modified_logo = logo.resize(width, height)
    return modified_logo


def main():
    