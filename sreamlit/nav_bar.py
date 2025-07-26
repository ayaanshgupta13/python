import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
import time

plt.style.use('ggplot')

data = {
    'num':[x for x in range(1,11)],
    'square':[x**2 for x in  range(1,11)],
    'twice':[x*2 for x in range(1,11)],
    'thrice':[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data = data)

rad=st.sidebar.radio("Navigation",['Home','us'])

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
    