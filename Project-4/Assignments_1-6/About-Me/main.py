import streamlit as st

st.title("About Me Using Streamlit")

st.write("Hello my name is Saad, Its my first time creating something using streamlit by myself.")

name = st.text_input("Enter your name: ")

if name:
    st.success(f"Hello {name}")

    if st.button("Click Me!"):
        st.balloons()
        



