from src.happynumbers import happy_number


import streamlit as st

st.title("Happy Number Checker")

number = st.number_input("Enter a positive integer:", min_value=1)

if st.button("Check"):
    if happy_number(number):
        st.success("This number is happy!")
    else:
        st.error("This number is not happy.")
