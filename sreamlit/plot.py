import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(

    np.random.randn(100,3),
    columns=['a','b','c']
)

# chart = alt.Chart(data).mark_circle().encode(
#     x = 'a' ,y='b'
# )

# st.altair_chart()

st.map()

st.graphviz_chart("""
digraph{
watch->like
like-> share
share->subscribe                                                       
share->watch                  

}
""")

plt.scatter(data['a'],data['b'])
plt.title('scatter')
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

st.image('dice-1.png')

st.audio('sreamlit//song.wav')