import tkinter as tk
from tkinter import messagebox, ttk
import csv
import datetime
import pandas as pd
from collections import defaultdict

# Function to add an item to inventory
def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    category = entry_category.get()

    if name and quantity.isdigit() and price.replace('.', '', 1).isdigit() and category:
        with open('inventory.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, quantity, price, category])
        messagebox.showinfo("Success", f"Item {name} added successfully!")
        show_inventory()
        clear_fields()
    else:
        messagebox.showerror("Error", "Please enter valid item details.")

# Function to show inventory in the treeview
def show_inventory(search_query=""):
    # Clear current entries
    for row in treeview_inventory.get_children():
        treeview_inventory.delete(row)

    try:
        with open('inventory.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # If there's a search query, check if the item name matches
                if search_query.lower() in row[0].lower() or search_query.lower() in row[2].lower():
                    treeview_inventory.insert("", "end", values=(row[0], row[1], row[2]))
    except FileNotFoundError:
        pass

# Function to clear the input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_category.delete(0, tk.END)

# Function to delete an item from inventory
def delete_item():
    selected_item = treeview_inventory.selection()
    if selected_item:
        item_name = treeview_inventory.item(selected_item)["values"][0]
        # Confirm deletion
        if messagebox.askyesno("Delete", f"Are you sure you want to delete item '{item_name}'?"):
            all_items = []
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)
                all_items = list(reader)
            
            # Remove item from the inventory list
            updated_items = [item for item in all_items if item[0] != item_name]

            with open('inventory.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_items)
            
            show_inventory()  # Refresh inventory view
            messagebox.showinfo("Success", f"Item '{item_name}' deleted successfully.")
    else:
        messagebox.showerror("Error", "Please select an item to delete.")

# Function to sell items and update the inventory
def sell_item():
    item_name = entry_sell_name.get()
    sell_quantity = entry_sell_quantity.get()

    if not sell_quantity.isdigit() or int(sell_quantity) <= 0:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    updated_inventory = []
    item_found = False
    total_cost = 0

    try:
        with open('inventory.csv', 'r') as file:
            reader = csv.reader(file)
            updated_inventory = list(reader)
        
        # Find the item in the inventory and update its quantity
        for i, row in enumerate(updated_inventory):
            if row[0] == item_name:
                item_found = True
                current_quantity = int(row[1])
                price_per_item = float(row[2])

                if current_quantity >= int(sell_quantity):
                    new_quantity = current_quantity - int(sell_quantity)
                    updated_inventory[i][1] = str(new_quantity)  # Update quantity

                    total_cost = price_per_item * int(sell_quantity)

                    # Log the transaction
                    with open('transactions.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([item_name, sell_quantity, price_per_item, total_cost, str(datetime.datetime.now())])

                    messagebox.showinfo("Sale Success", f"Sold {sell_quantity} of {item_name} for ${total_cost:.2f}")
                else:
                    messagebox.showerror("Error", f"Not enough quantity available. Only {current_quantity} left.")
                break
        
        if not item_found:
            messagebox.showerror("Error", "Item not found in inventory.")

        # Save the updated inventory to the file
        with open('inventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_inventory)
        
        show_inventory()
        clear_sell_fields()

    except FileNotFoundError:
        messagebox.showerror("Error", "Inventory file not found.")

# Function to clear the sell input fields
def clear_sell_fields():
    entry_sell_name.delete(0, tk.END)
    entry_sell_quantity.delete(0, tk.END)

# Function to show transaction history in treeview
def show_transactions():
    window_transactions = tk.Toplevel(window)
    window_transactions.title("Transaction History")
    
    treeview_transactions = ttk.Treeview(window_transactions, columns=("Item", "Quantity", "Price", "Total", "Date"), show="headings")
    treeview_transactions.pack(fill=tk.BOTH, expand=True)

    # Define column headings
    treeview_transactions.heading("Item", text="Item Name")
    treeview_transactions.heading("Quantity", text="Quantity Sold")
    treeview_transactions.heading("Price", text="Price per Item")
    treeview_transactions.heading("Total", text="Total Sale")
    treeview_transactions.heading("Date", text="Date")

    try:
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                treeview_transactions.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
    except FileNotFoundError:
        messagebox.showerror("Error", "No transaction history found.")

# Function to show sales summary (total sales, most sold items)
def show_sales_summary():
    try:
        # Load transaction data into pandas DataFrame
        transactions_df = pd.read_csv('transactions.csv', names=["Item", "Quantity", "Price", "Total", "Date"])

        # Calculate total sales
        total_sales = transactions_df["Total"].sum()

        # Calculate most sold items (by quantity)
        most_sold_items = transactions_df.groupby("Item")["Quantity"].sum().sort_values(ascending=False).head(5)

        summary = f"Total Sales: ${total_sales:.2f}\n"
        summary += "Most Sold Items:\n"

        for item, qty in most_sold_items.items():
            summary += f"{item}: {qty} sold\n"

        messagebox.showinfo("Sales Summary", summary)
    except FileNotFoundError:
        messagebox.showerror("Error", "No transaction history found.")

# Function to show sales trend (using pandas)
def show_sales_trend():
    try:
        # Load transaction data into pandas DataFrame
        transactions_df = pd.read_csv('transactions.csv', names=["Item", "Quantity", "Price", "Total", "Date"])

        # Convert 'Date' to datetime format
        transactions_df['Date'] = pd.to_datetime(transactions_df['Date'])

        # Group by date and calculate total sales per day
        daily_sales = transactions_df.groupby(transactions_df['Date'].dt.date)['Total'].sum()

        # Create a simple summary of daily sales
        sales_summary = f"Sales Trend:\n{daily_sales}"

        messagebox.showinfo("Sales Trend", sales_summary)
    except FileNotFoundError:
        messagebox.showerror("Error", "No transaction history found.")

# Initialize main window
window = tk.Tk()
window.title("Advanced Inventory & Billing System")

# Set up window color scheme
window.config(bg="#f0f0f0")

# Set up a notebook (tabbed interface)
notebook = ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)

# --- Add Item Tab ---
tab_add_item = ttk.Frame(notebook, style="Tab.TFrame")
notebook.add(tab_add_item, text="Add Item")

label_name = tk.Label(tab_add_item, text="Item Name:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(tab_add_item, font=("Arial", 12), bd=2, relief="solid")
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_quantity = tk.Label(tab_add_item, text="Quantity:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_quantity.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_quantity = tk.Entry(tab_add_item, font=("Arial", 12), bd=2, relief="solid")
entry_quantity.grid(row=1, column=1, padx=10, pady=5)

label_price = tk.Label(tab_add_item, text="Price per Item:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_price.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_price = tk.Entry(tab_add_item, font=("Arial", 12), bd=2, relief="solid")
entry_price.grid(row=2, column=1, padx=10, pady=5)

label_category = tk.Label(tab_add_item, text="Category:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_category.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_category = tk.Entry(tab_add_item, font=("Arial", 12), bd=2, relief="solid")
entry_category.grid(row=3, column=1, padx=10, pady=5)

button_add = tk.Button(tab_add_item, text="Add Item", command=add_item, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="solid", bd=2)
button_add.grid(row=4, column=0, columnspan=2, pady=10)

# --- Inventory Tab ---
tab_inventory = ttk.Frame(notebook, style="Tab.TFrame")
notebook.add(tab_inventory, text="Inventory")

treeview_inventory = ttk.Treeview(tab_inventory, columns=("Item", "Quantity", "Price", "Category"), show="headings", style="Custom.Treeview")
treeview_inventory.pack(fill=tk.BOTH, expand=True)

treeview_inventory.heading("Item", text="Item Name")
treeview_inventory.heading("Quantity", text="Quantity")
treeview_inventory.heading("Price", text="Price per Item")
treeview_inventory.heading("Category", text="Category")

show_inventory()  # Show initial inventory

# --- Search Box ---
search_label = tk.Label(tab_inventory, text="Search Item:", bg="#f0f0f0", font=("Arial", 12, "bold"))
search_label.pack(pady=10)

search_entry = tk.Entry(tab_inventory, font=("Arial", 12), bd=2, relief="solid")
search_entry.pack(pady=5)

def search_inventory():
    query = search_entry.get()
    show_inventory(query)

search_button = tk.Button(tab_inventory, text="Search", command=search_inventory, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), relief="solid", bd=2)
search_button.pack(pady=10)

# --- Billing Tab ---
tab_billing = ttk.Frame(notebook, style="Tab.TFrame")
notebook.add(tab_billing, text="Billing")

label_sell_name = tk.Label(tab_billing, text="Item Name to Sell:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_sell_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_sell_name = tk.Entry(tab_billing, font=("Arial", 12), bd=2, relief="solid")
entry_sell_name.grid(row=0, column=1, padx=10, pady=5)

label_sell_quantity = tk.Label(tab_billing, text="Quantity to Sell:", bg="#f0f0f0", font=("Arial", 12, "bold"))
label_sell_quantity.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_sell_quantity = tk.Entry(tab_billing, font=("Arial", 12), bd=2, relief="solid")
entry_sell_quantity.grid(row=1, column=1, padx=10, pady=5)

button_sell = tk.Button(tab_billing, text="Sell Item", command=sell_item, bg="#f44336", fg="white", font=("Arial", 12, "bold"), relief="solid", bd=2)
button_sell.grid(row=2, column=0, columnspan=2, pady=10)

# --- Additional Features ---
button_sales_summary = tk.Button(tab_billing, text="Show Sales Summary", command=show_sales_summary, bg="#FF9800", fg="white", font=("Arial", 12, "bold"), relief="solid", bd=2)
button_sales_summary.grid(row=3, column=0, columnspan=2, pady=10)

button_sales_trend = tk.Button(tab_billing, text="Show Sales Trend", command=show_sales_trend, bg="#FF5722", fg="white", font=("Arial", 12, "bold"), relief="solid", bd=2)
button_sales_trend.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
