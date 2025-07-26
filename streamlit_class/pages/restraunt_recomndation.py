from streamlit_option_menu import option_menu
import time
import streamlit as st
from streamlit_modal import Modal
import random

# Page Configuration
st.set_page_config(page_title="Streamlit Filter Panel", layout="wide")

sample_images = [
    "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/mcd.png", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/subway.jpg", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/hiras.png", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/tropical-leaves.png"
]


prefixes = ["The", "Cafe", "Bistro", "Spice", "Flavors", "Tandoori", "Royal", "Fusion", "Urban", "Heritage"]
main_words = ["Grill", "Kitchen", "Diner", "Hut", "House", "Garden", "Lounge", "Eatery", "Table", "Point"]
suffixes = ["Delight", "Express", "Corner", "Hub", "Treats", "Palace", "Nest", "Club", "Cove", "Retreat"]


restaurants = [
    {
        "name": f"{random.choice(prefixes)} {random.choice(main_words)} {random.choice(suffixes)}",
        "rating": round(random.uniform(3.0, 5.0), 1),  # Random rating 3.0 - 5.0
        "time": f"{random.randint(20, 50)}-{random.randint(30, 60)} MINS",
        "price": f"₹{random.randint(200, 1000)} FOR TWO",
        "cuisine": random.choice(["Italian", "Chinese", "Thai", "Indian", "French", "Japanese", "Mexican", "Spanish", "Korean"]),
        "image": random.choice(sample_images)
    }
    for i in range(1, 1000)  # Generate 1000 restaurants
]

st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #252525;
            color: white;
        }
        .stButton>button {
            background-color: #444;
            color: white;
            border-radius: 5px;
            padding: 5px 15px;
        }
        .stButton>button:hover {
            background-color: #666;
        }
        .modal-content {
            background-color: white;
            color: black;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="restraunt app",  # No title
        options=["Home"],
        icons=["info"]
    )

if "filters" not in st.session_state:
    st.session_state.filters = {"cuisine": None, "rating": None}

if selected == "Home":

    # Modal for Filters
    modal = Modal("Filter", key="filter_modal", max_width=600)
    temp_filters = {"cuisine": None, "rating": None}

    if st.button("Open Filter"):
        modal.open()

    if modal.is_open():
        with modal.container():
            st.markdown("<h3 style='text-align: center;'>Filter</h3>", unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                selected_option = st.radio(
                    "",
                    ["Delivery Time", "Cuisines", "Ratings", "Veg/Non-Veg"],
                    index=None,
                    key="filter_choice"
                )
                if selected_option == "Cuisines":
                    with col2:
                        temp_filters["cuisine"] = st.radio("Select Cuisine", ["Italian", "Chinese", "Thai", "Indian", "French", "Japanese", "Mexican", "Spanish", "Korean"], index=None)
                elif selected_option == "Ratings":
                    with col2:
                        temp_filters["rating"] = st.radio("Select Rating", [1, 2, 3, 4, 5], index=None)
                elif selected_option == "Veg/Non-Veg":
                    with col2:
                        temp_filters["Veg/Non-Veg"] = st.radio("Select Veg/Non-Veg", ["Veg","Non-Veg"], index=None)
                elif selected_option == "Delivery Time":
                    with col2:
                        temp_filters["Delivery Time"] = st.time_input("Select Delivery Time")


            st.markdown("<br>", unsafe_allow_html=True)
            
            col_buttons = st.columns([1, 1])
            
            with col_buttons[0]:
                if st.button("Apply", use_container_width=True):
                    if temp_filters["cuisine"]:
                        st.session_state.filters["cuisine"] = temp_filters["cuisine"]
                    if temp_filters["rating"]:
                        st.session_state.filters["rating"] = temp_filters["rating"]
                    st.success("Filters applied!")
                    st.rerun()

            with col_buttons[1]:
                if st.button("Close", use_container_width=True):
                    modal.close()

    # Apply Filters to Restaurant List
    filtered_restaurants = restaurants
    if st.session_state.filters["cuisine"]:
        filtered_restaurants = [r for r in filtered_restaurants if r["cuisine"] == st.session_state.filters["cuisine"]]
    if st.session_state.filters["rating"]:
        filtered_restaurants = [r for r in filtered_restaurants if r["rating"] >= st.session_state.filters["rating"]]

    st.markdown("<h2>🍽️ Top 1000+ Restaurants in Delhi</h2>", unsafe_allow_html=True)
 
    cols = st.columns(3)

    for index, restaurant in enumerate(filtered_restaurants):
        with cols[index % 3]:
            with st.container():
                st.image(restaurant["image"], width=100)
                st.markdown(f"""
                <h4 style="margin-bottom: 5px;">{restaurant["name"]}</h4>
                ⭐ {restaurant["rating"]} · ⏳ {restaurant["time"]} · {restaurant["price"]}<br>
                <span style="color: grey;">{restaurant["cuisine"]}</span>
                """, unsafe_allow_html=True)
                st.link_button("Visit Restaurant", "http://localhost:8502/")

