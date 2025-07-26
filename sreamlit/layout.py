import streamlit as st
import time

st.title('form')



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
    