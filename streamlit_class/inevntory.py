import streamlit as st
import csv
import datetime
import pandas as pd

# Function to load inventory
def load_inventory():
    try:
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Function to update inventory
def update_inventory(updated_inventory):
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_inventory)

# Function to log transactions
def log_transaction(item_name, quantity, price, total, date, payment_method, address):
    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item_name, quantity, price, total, date, payment_method, address])

# Streamlit App
st.title("Advanced Inventory & Billing System")

# Tabs for Navigation
tabs = ["Add Item", "View Inventory", "Sell Item", "Transaction History"]
choice = st.sidebar.selectbox("Select a Page", tabs)

if choice == "Add Item":
    st.header("Add New Item to Inventory")
    item_name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price per Item", min_value=0.0, step=0.01)
    category = st.text_input("Category")

    if st.button("Add Item"):
        if item_name and category:
            with open("inventory.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([item_name, quantity, price, category])
            st.success(f"Item '{item_name}' added successfully!")
        else:
            st.error("Please enter all required details.")

elif choice == "Sell Item":
    st.header("Sell an Item")
    inventory = load_inventory()
    item_names = [item[0] for item in inventory]
    selected_item = st.selectbox("Select Item", item_names)
    quantity_to_sell = st.number_input("Quantity to Sell", min_value=1, step=1)
    payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Online Payment"])
    shipping_address = st.text_area("Shipping Address")
    sale_date = st.date_input("Sale Date", datetime.date.today())

    if st.button("Sell Item"):
        updated_inventory = []
        total_cost = 0
        item_found = False

        for item in inventory:
            if item[0] == selected_item:
                item_found = True
                current_quantity = int(item[1])
                price_per_item = float(item[2])
                
                if current_quantity >= quantity_to_sell:
                    new_quantity = current_quantity - quantity_to_sell
                    item[1] = str(new_quantity)
                    total_cost = price_per_item * quantity_to_sell
                    log_transaction(selected_item, quantity_to_sell, price_per_item, total_cost, sale_date, payment_method, shipping_address)
                    st.success(f"Sold {quantity_to_sell} of {selected_item} for ${total_cost:.2f}")
                else:
                    st.error(f"Not enough stock. Only {current_quantity} available.")
            updated_inventory.append(item)

        if not item_found:
            st.error("Item not found in inventory.")

        update_inventory(updated_inventory)
