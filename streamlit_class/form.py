import streamlit as st
from datetime import date

col1,col2 = st.columns(2)

with col1:
    with st.form(key = "newForm"):
        textbox = st.text_input(label="enter your name")
        submit = st.form_submit_button()

    if submit:
        st.write(f"hello {textbox}")
with col2:
    with st.form(key = "form"):
        color = st.selectbox('colors',['orange','black','cyan',"red",'green'])
        submit = st.form_submit_button()
        val = st.slider(label="color darkness",min_value=0,max_value=100)
    if submit:
        st.write(f"{color} is your favourite with {val} darkness")


with st.form(key="form3"):
    cols = st.columns(3)
    for i,col in enumerate(cols):
        if i == 0:
            age = col.text_input("enter your age")
        elif i == 1:
            food = col.selectbox("food preference",["veg",'nonveg'])
        elif i == 2:
            weight = col.slider("select your weight",min_value=10,max_value=500)

    submit = st.form_submit_button()


with st.form(key = "addition"):
    x = st.number_input("enter first number: ")
    y = st.number_input("enter second number: ")
    add = st.form_submit_button("add")
    if add:
        st.write(f"the sum is :blue[{x+y}]")

    sub = st.form_submit_button("subtract")
    if sub:
        st.write(f"the sum is :blue[{x-y}]")

    multiply = st.form_submit_button("multiply")
    if multiply:
        st.write(f"the sum is :blue[{x*y}]")

with st.form(key = "color"):
    option = ["code","swim","read","dance","sing"]
    r = st.radio("choose a hobby",option)
    submit = st.form_submit_button()
    if submit:
        st.write(f"your hobby is {r}")

with st.form(key="age"):
    birthdate = st.date_input("Enter your birthdate:", min_value=date(1900, 1, 1), max_value=date.today())

    submit = st.form_submit_button("Calculate Age")

    if submit:
        if birthdate > date.today():
            st.error("Birthdate cannot be in the future!")
        else:
            today = date.today()
            age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            
            # Correcting the last birthday calculation
            last_birthday = birthdate.replace(year=today.year)
            if last_birthday > today:
                last_birthday = birthdate.replace(year=today.year - 1)
                
            age_days = (today - last_birthday).days  # Days since last birthday
            
            st.success(f"Your age is: {age_years} years and {age_days} days ")