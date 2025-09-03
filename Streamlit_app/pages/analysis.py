import streamlit as st
from utils.calculations import filter_by_threshold, summarize_by_category
from components.tables import display_summary

def main():
    st.title("📊 Analysis Page")
    threshold = st.slider("Value Threshold", 0, 100, 50)
    
    df = st.session_state.df
    filtered_df = filter_by_threshold(df, threshold)
    summary_df = summarize_by_category(filtered_df)
    
    display_summary(summary_df, "Average Value by Category")

if __name__ == "__main__":
    main()
