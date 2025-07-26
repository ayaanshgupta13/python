import streamlit as st

st.title('hello')
st.header('header')
st.subheader('sub header')
st.text('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
#refer to markdown cheatsheet
st.markdown(""" # h1
## h2
:sunglasses:<br>
:moon:<br>
**bold**<br>
_italic_
""",True)

dic = {
    'name':'ayaansh',
    'age':11,
    'city':'gurugram'
}

st.dataframe(dic)
st.table(dic)
st.json(dic)
st.write(dic)

mycode='''
print("hello World")
def mysong():
    return 0
'''
st.code(mycode)
st.image("lamborgini-gdd8223bd8_640.jpg",caption="lamborgini")
st.audio("song.mp3")
st.audio_input("record your voice")
# st.write('ayaansh gupta')

st.markdown("""
|             | mon         | tue           |
| :---        |    :----:   |          ---: |
| 1           | math        | SST           |
| 2           | science     | english       |

""")