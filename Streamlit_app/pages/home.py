import streamlit as st
from utils.calculations import filter_by_threshold
from components.tables import display_dataframe

def main():
    st.title("🏠 Home Page")
    threshold = st.slider("Value Threshold", 0, 100, 50)
    
    df = st.session_state.df
    filtered_df = filter_by_threshold(df, threshold)
    
    display_dataframe(filtered_df, "Filtered Data")

if __name__ == "__main__":
    main()
