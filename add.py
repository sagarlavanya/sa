# streamlit_fun_adding_app.py

import streamlit as st

# Set up the app title with colorful text and emojis
st.markdown("<h1 style='text-align: center; color: purple;'>🎉 Fun Adding App for Toddlers 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: orange;'>Let's add two numbers together!</h3>", unsafe_allow_html=True)

# Use Streamlit's number inputs for toddler-friendly input handling
first_number = st.number_input("Enter the first number:", min_value=0, step=1, key="first")
second_number = st.number_input("Enter the second number:", min_value=0, step=1, key="second")

# Add a button to calculate the sum
if st.button("Calculate Sum 💡"):
    # Calculate the sum
    result = first_number + second_number
    
    # Display the result with colorful styling
    st.markdown(f"<h2 style='text-align: center; color: green;'>🎈 The sum is: {result} 🎈</h2>", unsafe_allow_html=True)
    st.balloons()  # Adds a fun balloon animation
