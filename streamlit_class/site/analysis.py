import streamlit as st
import pandas as pd
import numpy as np



def app():
    st.title("Data Analysis")
    file = st.file_uploader("upload csv",type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write("### Data preview")
        st.dataframe(df.head())
        st.write("### Data stats")
        st.dataframe(df.describe())
        st.write("### Column Selection")
        column = st.selectbox("choose a numeric column to plot",df.select_dtypes(include=np.number).columns)
        if column:
            st.line_chart(df[column])