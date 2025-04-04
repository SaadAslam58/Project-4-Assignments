import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploade_file = st.file_uploader("Choose a CSV file", type="csv")

if uploade_file is not None:
    df = pd.read_csv(uploade_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by", columns)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select values", unique_value)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_columns = st.selectbox("Select 'X' columns", columns)
    y_columns = st.selectbox("Select 'Y' columns", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_columns)[y_columns])
else:
    st.info("Please upload a CSV file.")