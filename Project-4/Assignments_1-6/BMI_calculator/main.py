import streamlit as st

st.title("BMI Calculator🧮")


heigth = st.slider("Enter your height in centimeters (cm).", 100, 250, 160)
weigth = st.slider("Enter your width in kg.", 40, 150, 70)

bmi = weigth / ((heigth / 100)**2)

if st.button("Calculate"):
    if bmi < 18.5:
        st.image()
        st.info(f"Your BMI is {bmi:.2f}, you are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        st.info(f"Your BMI is {bmi:.2f}, you have a normal weight.")
    elif bmi >= 25 and bmi < 29.9:
        st.info(f"Your BMI is {bmi:.2f}, you are overweight.")                   
    elif bmi >= 30:
        st.info(f"Your BMI is {bmi:.2f}, you are obese.")
    
st.subheader(" BMI Catogaries ###")
st.write("Underweight: BMI < 18.5")
st.write("Normal weight: BMI > 18.5 and BMI < 24.9")
st.write("Overweight: BMI > 25 and BMI < 29.9")
st.write("Obese: BMI > 30")
