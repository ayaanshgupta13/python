import streamlit as st

st.sidebar.title("Travel navigation")

st.write("travel info made easy")

n =st.sidebar.text_input("enter your name")

num = st.sidebar.slider("selct buget",100,100000,50000)

t =st.sidebar.number_input("amount of travellers",min_value = 1)



p=st.sidebar.radio('site',['mountain','beach','city',"desert"])

if st.sidebar.button("submit"):
    st.write(f"hi {n}, you are traveling to {p} with {t} people")



with st.sidebar.expander(' Other Travel options: ' ) :
    travel = st.selectbox( 'Choose option' ,[ ' Air' , 'Train','Road ' ] )


st.write(f"your buget is {num}")
st.write(f"you wish to travel by {travel}")



