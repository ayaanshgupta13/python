import streamlit as st

st.title("Restaurant Reservation Form")

with st.form("reserve"):
    
    name = st.text_input("What is your name?")
    contact_number = st.text_input("Enter your contact number:")
        
    restaurant_location = st.selectbox("Select the restaurant location:", ["Location 1", "Location 2", "Location 3"])  # Add actual locations
    dining_date = st.date_input("Choose your preferred dining date:")
    time_slot = st.time_input("Select your preferred time slot:")
        
    group_size = st.number_input("How many people are in your group?", min_value=1, step=1)
    seating_preference = st.radio("Do you prefer indoor or outdoor seating?", ["Indoor", "Outdoor"],index=None)
        
    cuisine_preferences = st.text_input("Do you have any cuisine preferences? (Italian, Chinese, Indian, etc.)")
    dietary_restrictions = st.text_area("Do you have any dietary restrictions or allergies?")
        
    special_occasion = st.text_input("Would you like a special occasion setup? (Birthday, Anniversary, etc.)")
    private_dining = st.radio("Do you need a private dining area?", ["Yes", "No"],index=None)
    pre_order_meals = st.radio("Would you like to pre-order meals?", ["Yes", "No"],index=None)
    parking_assistance = st.radio("Do you require parking assistance?", ["Yes", "No"],index=None)
    confirmation_method = st.radio("Would you like to receive a confirmation via email or SMS?", ["Email", "SMS"],index=None)
        
    special_requests = st.text_area("Any special requests or additional notes?")
        
    if st.form_submit_button("Submit Reservation"):
        st.success("Thank you for your reservation! We will confirm your booking shortly.")
        