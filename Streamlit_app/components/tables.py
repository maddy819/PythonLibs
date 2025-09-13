import streamlit as st

def display_dataframe(df, title="Data"):
    st.subheader(title)
    st.dataframe(df)

def display_summary(summary_df, title="Summary"):
    st.subheader(title)
    st.table(summary_df)
