import streamlit as st
import pandas as pd

st.set_page_config(page_title="Introduction", layout="wide")

df = pd.read_csv("House_clean_data.csv")

st.title("House Power Consumption Analysis")

st.header("Project Introduction")

st.write("""
This project analyzes household power consumption data using Python and Streamlit.
The dataset contains information about electrical power usage, voltage, current,
sub-meter readings, date, time, year, month, hour, and day of the week.

The objective of this project is to understand electricity usage patterns
through different visualizations and statistical analysis.
""")

st.header("Dataset Overview")

st.write("Rows :", df.shape[0])
st.write("Columns :", df.shape[1])

st.subheader("Column Names")

st.write(list(df.columns))

st.subheader("First Five Records")

st.dataframe(df.head())