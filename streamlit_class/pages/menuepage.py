import streamlit as st

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Sample menu items
menu = {
    "Appetizers": {
        "Garlic Bread": 5.99,
        "Bruschetta": 7.99,
        "Mozzarella Sticks": 6.99
    },
    "Main Course": {
        "Margherita Pizza": 12.99,
        "Pasta Alfredo": 14.99,
        "Grilled Salmon": 18.99
    },
    "Desserts": {
        "Tiramisu": 6.99,
        "Cheesecake": 5.99,
        "Chocolate Lava Cake": 7.99
    },
    "Drinks": {
        "Coke": 1.99,
        "Lemonade": 2.99,
        "Coffee": 3.49
    }
}

st.title("Restaurant Menu")
st.write("Browse our delicious menu and add items to your cart!")

# Display menu
for category, items in menu.items():
    st.subheader(category)
    for item, price in items.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{item} - ${price:.2f}")
        with col2:
            if st.button(f"Add {item}", key=item):
                if item in st.session_state.cart:
                    st.session_state.cart[item]['quantity'] += 1
                else:
                    st.session_state.cart[item] = {'price': price, 'quantity': 1}
                st.success(f"{item} added to cart!")

# Sidebar Cart
st.sidebar.header("🛒 Your Cart")
total = 0
if st.session_state.cart:
    for item, details in st.session_state.cart.items():
        qty = details['quantity']
        price = details['price']
        subtotal = qty * price
        total += subtotal
        st.sidebar.write(f"{item} ({qty}) - ${subtotal:.2f}")
    st.sidebar.write("---")
    st.sidebar.write(f"**Total: ${total:.2f}**")
    if st.sidebar.button("Checkout"):
        st.session_state.cart.clear()
        st.sidebar.success("Order placed successfully!")
else:
    st.sidebar.write("Your cart is empty.")
