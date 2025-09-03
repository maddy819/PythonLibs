import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Sales Dashboard", layout="wide")

# Dummy Data
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        "Date": pd.date_range("2024-01-01", periods=60),
        "Region": ["North", "South", "East", "West"] * 15,
        "Product": ["Chai", "Coffee", "Green Tea", "Black Tea", "Herbal Tea", "Oolong Tea", "White Tea", "Matcha", "Lemon Tea", "Peach Tea"] * 6,
        "Revenue": np.random.randint(500, 3000, 60),
        "Units_Sold": np.random.randint(20, 100, 60)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
product_filter = st.sidebar.multiselect("Select Product", df["Product"].unique(), default=df["Product"].unique())

# Filter Data
filtered_df = df[df["Region"].isin(region_filter) & df["Product"].isin(product_filter)]

# KPI Section
st.title("📈 Simple Sales Dashboard")

total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Units_Sold"].sum()
avg_units = filtered_df["Units_Sold"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Products", filtered_df["Product"].nunique())
col2.metric("Total Revenue", f"₹{total_revenue:,}")
col3.metric("Total Units Sold", total_units)
col4.metric("Avg Units per Day", f"{avg_units:.2f}")

st.markdown("---")

chartcol1, chartcol2 = st.columns(2)

# Revenue by Product using built-in bar chart
chartcol1.subheader("Revenue by Product")
revenue_chart = filtered_df.groupby("Product")["Revenue"].sum()
chartcol1.bar_chart(revenue_chart)

# Units Sold Over Time using line chart
chartcol2.subheader("Units Sold Over Time")
units_time = filtered_df.groupby("Date")["Units_Sold"].sum()
chartcol2.line_chart(units_time)

st.markdown("---")

# Page size
page_size = 10

# Number of pages
total_pages = (len(filtered_df) - 1) // page_size + 1

# Keep track of current page in session state
if "page" not in st.session_state:
    st.session_state.page = 1

tabcol1, tabcol2 = st.columns(2)

# Show Table
tabcol1.subheader("Raw Data")
# Slice DataFrame for current page
start = (st.session_state.page - 1) * page_size
end = start + page_size
tabcol1.dataframe(filtered_df.sort_values(by="Date", ascending=False).iloc[start:end], use_container_width=True)

# Navigation buttons
col1, col2, col3 = tabcol1.columns([8,2,2])

with col1:
    if st.button("⬅️ Previous") and st.session_state.page > 1:
        st.session_state.page -= 1

with col2:
    st.write(f"Page {st.session_state.page} of {total_pages}")

with col3:
    if st.button("Next ➡️") and st.session_state.page < total_pages:
        st.session_state.page += 1


tabcol2.subheader("Raw Statistics")
df_description = df.iloc[:, 3:].describe()
tabcol2.dataframe(df_description, use_container_width=True)
