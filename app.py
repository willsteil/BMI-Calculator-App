
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")
st.write("Enter your weight (kg) and height (meters) to calculate BMI.")

# User Inputs
weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Height (meters)", min_value=0.0, format="%.2f")

# BMI Calculation
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        # BMI Categories
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            st.info("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.error("Height must be greater than 0")
