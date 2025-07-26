# import tkinter module
import streamlit as st
import csv

rad=st.sidebar.radio("Navigation",["add stock","stock",'billing'])



if rad == "add stock":

    name,price,quantity = st.columns(3)

    n = name.text_input("name of the product")
    p = price.number_input("price of the product")
    q = quantity.number_input("quantity of the product")

    stock = str({
        "name":n,
        "price":p,
        "quantity":q
    })



    add = st.button("add")

    if add:
        with open("stock.CSV", "a",newline='') as file:
            writer = csv.writer(file)

            writer.writerows(stock)
        st.success("your product id added")
    

if rad == "stock":
    f = open("stock.CSV", "r")
    
    st.table(f)
     
        