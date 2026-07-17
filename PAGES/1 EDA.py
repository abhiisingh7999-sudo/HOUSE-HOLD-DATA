import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDA", layout="wide")

df = pd.read_csv("House_clean_data.csv")

st.title("Exploratory Data Analysis")

tab1, tab2, tab3 = st.tabs(["Dataset", "Visualizations", "Insights"])

with tab1:

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.subheader("Data Types")
    st.dataframe(df.dtypes.astype(str))

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

with tab2:

    numeric = df.select_dtypes(include="number").columns.tolist()

    st.subheader("Correlation Heatmap")

    fig = px.imshow(
        df[numeric].corr(),
        text_auto=True,
        color_continuous_scale="Viridis",
        aspect="auto"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Interactive Scatter Plot")

    c1, c2 = st.columns(2)

    x = c1.selectbox("X-axis", numeric)
    y = c2.selectbox("Y-axis", numeric, index=1)

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color="DayName",
        hover_data=df.columns
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Distribution")

    feature = st.selectbox("Select Feature", numeric)

    fig = px.histogram(
        df,
        x=feature,
        nbins=40,
        marginal="box"
    )

    st.plotly_chart(fig, use_container_width=True)

    if "Hour" in df.columns:

        st.subheader("Average Value by Hour")

        value = st.selectbox(
            "Select Numeric Column",
            numeric,
            key="hour"
        )

        temp = df.groupby("Hour")[value].mean().reset_index()

        fig = px.line(
            temp,
            x="Hour",
            y=value,
            markers=True
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Day" in df.columns:

        st.subheader("Records by Day")

        fig = px.pie(
            df,
            names="Day"
        )

        st.plotly_chart(fig, use_container_width=True)

with tab3:

    st.subheader("Key Insights")

    st.write("- The dataset contains household electricity consumption measurements.")
    st.write("- Correlation heatmap shows relationships among electrical variables.")
    st.write("- Scatter plots help identify trends and outliers.")
    st.write("- Hourly line charts show how power usage changes during the day.")
    st.write("- Distribution plots reveal the spread of each numerical feature.")
    st.write("- Pie chart displays the proportion of records for each day.")

st.download_button(
    label="Download Dataset",
    data=df.to_csv(index=False),
    file_name="House_clean_data.csv",
    mime="text/csv"
)