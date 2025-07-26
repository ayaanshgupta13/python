import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Top Restaurants", layout="wide")

# Sample images (Replace with actual images)
sample_images = [
    "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/mcd.png", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/subway.jpg", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/hiras.png", "C:/Users/neera/OneDrive/Desktop/python/streamlit_class/images/tropical-leaves.png"
]

# Generate 1000 restaurants dynamically
restaurants = [
    {
        "name": f"Restaurant {i}",
        "rating": round(random.uniform(3.0, 5.0), 1),  # Random rating 3.0 - 5.0
        "time": f"{random.randint(20, 50)}-{random.randint(30, 60)} MINS",
        "price": f"₹{random.randint(200, 1000)} FOR TWO",
        "cuisine": random.choice(["Indian", "Chinese", "Italian", "Mexican", "American"]),
        "image": random.choice(sample_images),
        "link": f"https://restaurant{i}.com"
    }
    for i in range(1, 1001)  # Generate 1000 restaurants
]

# Title
st.markdown("<h2>🍽️ Top 1000+ Restaurants in Delhi</h2>", unsafe_allow_html=True)

# Create a scrollable grid layout (3 columns)
cols = st.columns(3)  

# Display restaurants in a grid
for index, restaurant in enumerate(restaurants):
    with cols[index % 3]:  # Distribute in 3 columns
        with st.container():
            col1, col2 = st.columns([1, 3])  # Left: Image, Right: Details

            with col1:
                # Clickable image using st.image
                st.markdown(
                    f'<a href="{restaurant["link"]}" target="_blank">',
                    unsafe_allow_html=True
                )
                st.image(restaurant["image"], width=100)
                st.markdown("</a>", unsafe_allow_html=True)

            with col2:
                # Restaurant details
                st.markdown(f"""
                <h4 style="margin-bottom: 5px;">{restaurant["name"]}</h4>
                ⭐ {restaurant["rating"]} · ⏳ {restaurant["time"]} · {restaurant["price"]}<br>
                <span style="color: grey;">{restaurant["cuisine"]}</span>
                """, unsafe_allow_html=True)

