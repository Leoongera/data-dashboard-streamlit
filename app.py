import streamlit as st
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)

data = pd.DataFrame({
    "Region": np.random.choice(["North", "South", "East", "West"], 200),
    "Product": np.random.choice(["A", "B", "C"], 200),
    "Revenue": np.random.randint(100, 1000, 200)
})

st.title("Business Data Dashboard")

# Sidebar filters
region_filter = st.sidebar.selectbox("Select Region", ["All"] + list(data["Region"].unique()))

if region_filter != "All":
    data = data[data["Region"] == region_filter]

# Metrics
st.subheader("Total Revenue")
st.write(data["Revenue"].sum())

# Charts
st.subheader("Revenue by Region")
st.bar_chart(data.groupby("Region")["Revenue"].sum())

st.subheader("Revenue by Product")
st.bar_chart(data.groupby("Product")["Revenue"].sum())
