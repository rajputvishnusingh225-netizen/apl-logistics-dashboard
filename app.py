import streamlit as st
import pandas as pd

st.set_page_config(page_title="APL Logistics Dashboard", layout="wide")

st.title("📦 APL Logistics Dashboard")

# Load Data
df = pd.read_csv("APL_Logistics.csv", encoding="latin1")

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Rows", len(df))
col2.metric("Total Columns", len(df.columns))
col3.metric("Total Orders", df.shape[0])

# Sidebar Filters
st.sidebar.header("Filters")

if "Type" in df.columns:
    selected_type = st.sidebar.multiselect(
        "Select Order Type",
        options=df["Type"].dropna().unique(),
        default=df["Type"].dropna().unique()
    )

    df = df[df["Type"].isin(selected_type)]

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head(20))

# Column Names
with st.expander("Column Names"):
    st.write(df.columns.tolist())

# Summary Statistics
st.subheader("Dataset Summary")
st.write(df.describe(include="all"))

# Charts
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    st.subheader("Numeric Data Chart")

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    st.bar_chart(df[selected_col].head(50))