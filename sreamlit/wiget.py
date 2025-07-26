import streamlit as st

if st.button('subscribe'):
    st.write('like too')


name = st.text_input('name')
st.write(name)

address = st.text_area('enter your address')
st.write(address)

st.date_input('enter a date')
st.time_input('enter time input')

if st.checkbox('you accept T&C',value = False):
    st.write('thank you')

st.radio('colors',['a','b','c'])
st.selectbox('colors',['a','b','c'])

v3 = st.multiselect('colors',['a','b','c'])
st.write(v3)
st.slider('age')
# st.slider()/st.number_input()also takes arguments like min val,max val,val,step
st.number_input('numbers')

img = st.file_uploader('upload a file')
