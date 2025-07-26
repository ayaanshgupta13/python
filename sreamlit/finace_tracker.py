import streamlit as st
import pandas as pd 
# import matplotlib.pyplot as plt
import time



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

rad=st.sidebar.radio("Navigation",["home",'us','register'])


if rad == 'home':
    st.title('finance')
    user,pw,pw2 = st.columns(3)

    need = user.text_input('enter remark')
    amt = pw.text_input('enter amount')
    date = st.date_input('enter a date')
    
    

    finace = {
        "remark":need,
        "amount":amt,
        "date":date
    }
    st.write(finace)
    if st.button('confirm'):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        
        with open("bills.text", "a") as f:
            print(str(finace), file=f)
            # print("Line 2", file=f)
            # print("Line 3", file=f)
        # f = open("bills.text", "a")
        # f.write(str(finace))
            f.close()
        st.success('success, your bill is added to the data base')
        #open and read the file after the appending:
        
    if st.button('view all bills'):
        f = open("bills.text", "r")
        for x in f :
            st.table(finace)

    if st.button('clear all bills'):
        f = open("bills.text", "w")
        st.write(" ")

if rad == 'us':
    st.title('trial')
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
    if p1 == p2:
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
    else:
        st.error("pasword doesnt match")

    
        