import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conclusion", layout="wide")

df = pd.read_csv("House_clean_data.csv")

st.title("Project Conclusion")

st.write("""
The analysis of household power consumption provides useful insights into
electricity usage patterns.

Key Findings:

1. Global Active Power changes throughout the day.
2. Electricity usage varies with different hours.
3. Voltage remains comparatively stable.
4. Sub-meter readings help identify energy consumption in different sections.
5. Correlation analysis shows relationships between electrical variables.
6. The cleaned dataset is suitable for further analysis and machine learning.

This project demonstrates how Python, Pandas, Plotly, and Streamlit can be
used to analyze and visualize real-world datasets efficiently.
""")