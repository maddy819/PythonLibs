import streamlit as st
from utils.data_loader import generate_data

# Load data once (shared across pages)
if "df" not in st.session_state:
    st.session_state.df = generate_data(100)

st.title("Modular Multi-Page Streamlit App")
st.write("Use the sidebar to navigate pages.")
