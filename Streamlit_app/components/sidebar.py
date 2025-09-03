import streamlit as st

def select_page(pages):
    """Page navigation"""
    return st.sidebar.radio("Navigate", pages)

def value_slider(default=50):
    """Value threshold filter"""
    return st.sidebar.slider("Value Threshold", 0, 100, default)
