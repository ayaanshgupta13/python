import streamlit as st
import analysis , contact

st.set_page_config("my app",layout="wide")

st.sidebar.title("Navigation")

page = st.sidebar.radio("select a page",["analysis","contact"])


if page == "analysis":
    analysis.app()

elif page == "contact":
    contact.app()