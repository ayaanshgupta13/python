import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
import time

st.title('form')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

plt.style.use('ggplot')

data = {
    'num':[x for x in range(1,11)],
    'square':[x**2 for x in  range(1,11)],
    'twice':[x*2 for x in range(1,11)],
    'thrice':[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data = data)

rad=st.sidebar.radio("Navigation",['Home','us','register'])

if rad == 'home':


    st.sidebar.selectbox('select a number',[1,2,3,4,5,6,7,8,9,10])
    col = st.sidebar.multiselect('select a column',df.columns)

    plt.plot(df['num'],df[col])
    st.pyplot()

if rad == 'us':
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.error('error')
    st.success('success')
    st.info('info')
    st.exception(RuntimeError('error'))
    st.warning('warning')

if rad == 'register':

    


    first,last = st.columns(2)

    f = first.text_input('First Name')
    l = last.text_input('Last Name')



    email,mob = st.columns([3,1])

    e = email.text_input('Email ID')
    m = mob.text_input('Mob Number')


    user,pw,pw2 = st.columns(3)

    u = user.text_input('Username')
    p1 = pw.text_input('Password',type = 'password')
    p2 = pw2.text_input('retype your Password',type = 'password')


    ch,bl,sub = st.columns(3)

    c = ch.checkbox('I Agree')
    if sub.button('submit'):
        st.success('submited!')

        info = {
            'fname':f,
            'lname':l,
            'email':e,
            'mobile':m,
            'username':u,
            'password':p1,
            'T&C':c
        }
        st.table(info)

    b,con,b = st.columns(3)
    if con.button('confirm'):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)

    
        st.success('confirmed')
        